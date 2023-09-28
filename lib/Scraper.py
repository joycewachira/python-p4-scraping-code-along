# scraper.py
import requests
from bs4 import BeautifulSoup
from course import Course  # Import the Course class

class Scraper:
    def __init__(self):
        self.courses = []

    def get_page(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return BeautifulSoup(response.text, 'html.parser')
        else:
            print("Failed to retrieve the web page.")
            return None

    def extract_courses(self, page):
        courses = []
        course_elements = page.select('.post')
        for course_element in course_elements:
            title = course_element.select("h2")[0].text.strip()
            schedule = course_element.select(".date")[0].text.strip()
            description = course_element.select("p")[0].text.strip()
            courses.append(Course(title, schedule, description))
        return courses

    def scrape_courses(self, url):
        page = self.get_page(url)
        if page:
            self.courses = self.extract_courses(page)
            return self.courses

    def print_courses(self):
        for course in self.courses:
            print(course)