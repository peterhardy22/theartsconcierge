from bs4 import BeautifulSoup
import requests
import pandas as pd


def scrape_all():
    data = {}
    # MUSEUM SCRAPING
    # Function that scrapes Berkeley Art Museum Exhibit details
    def bampfa_scrape():
        # Request URL of Berkeley Art Museum Exhibits web page
        bampfa_page = requests.get(
            "https://bampfa.org/on-view?field_event_series_type_value=1&field_dates_value=2&field_dates_value2=2")
        # Creates soup for reading HTML content easier
        bampfa_soup = BeautifulSoup(bampfa_page.content, 'html.parser')
        # Initialize empty lists to store data
        titles = []
        dates = []
        images = []
        links = []
        # Create variable as block of HTML which has info we need
        exhibition_div = bampfa_soup.find_all(True, {'class': ['first odd', 'even', 'odd', 'last even']})
        # For loop to iterate through and extract data
        for container in exhibition_div:
            # Titles
            name = container.find('h2', class_='caption-txt').text
            name = name.replace('\n', '')
            titles.append(name)
            # Dates
            date = container.find('span', class_='dates').text
            dates.append(date)
            # Images
            image_url = container.find('img').get('src')
            images.append(image_url)
            # Links
            start_museum_url = 'https://bampfa.org'
            end_exhibit_url = container.find('a').get('href')
            exhibit_url = start_museum_url + end_exhibit_url
            links.append(exhibit_url)

        bampfa_exhibits = zip(titles, dates, images, links)

        bampfa_df = pd.DataFrame(bampfa_exhibits, columns=['title', 'dates', 'image', 'link'])
        bampfa_df.insert(0, 'institution', 'bampfa')

        return bampfa_df

    # Function that srapes de Young Exhibit details
    def deyoung_scrape():
        # Request URL of de Young Museum Exhibits web page
        deyoung_page = requests.get("https://deyoung.famsf.org/exhibitions")
        # Creates soup for reading HTML content easier
        deyoung_soup = BeautifulSoup(deyoung_page.content, 'html.parser')
        # Initialize empty lists to store data
        titles = []
        dates = []
        images = []
        links = []
        # Create variable as block of HTML which has info we need
        exhibition_div = deyoung_soup.find_all('div', class_='block--item')
        # For loop to iterate through and extract data
        for container in exhibition_div:
            # Titles
            name = container.h4.text
            titles.append(name)
            # Dates
            date = container.find('h6', class_='block--datevenue h8').text
            dates.append(date)
            # Images
            start_museum_url = 'https://deyoung.famsf.org'
            end_image_url = container.find('a', class_='content').get('data-img')
            image_url = start_museum_url + end_image_url
            images.append(image_url)
            # Links
            end_exhibit_url = container.find('a', class_='block--text').get('href')
            exhibit_url = start_museum_url + end_exhibit_url
            links.append(exhibit_url)

        deyoung_exhibits = zip(titles, dates, images, links)

        deyoung_df = pd.DataFrame(deyoung_exhibits, columns=['title', 'dates', 'image', 'link'])
        deyoung_df.insert(0, 'institution', 'deyoung')

        return deyoung_df

    # Function that scrapes Legion of Honor Exhibit details
    def legionofhonor_scrape():
        # Request URL of Legion of Honor Exhibits web page
        legionofhonor_page = requests.get("https://legionofhonor.famsf.org/exhibitions")
        # Creates soup for reading HTML content easier
        legion_soup = BeautifulSoup(legionofhonor_page.content, 'html.parser')
        # Initialize empty lists to store data
        titles = []
        dates = []
        images = []
        links = []
        # Create variable as block of HTML which has info we need
        exhibition_div = legion_soup.find_all('div', class_='block--item')
        # For loop to iterate through and extract data
        for container in exhibition_div:
            # Titles
            name = container.find('h4', class_='block--title h4').text
            titles.append(name)
            # Dates
            date = container.find('h6', class_='block--datevenue h8').text
            dates.append(date)
            # Images
            start_museum_url = 'https://legionofhonor.famsf.org'
            end_image_url = container.find('a', class_='content').get('data-img')
            image_url = start_museum_url + end_image_url
            images.append(image_url)
            # Links
            end_exhibit_url = container.find('a', class_='block--text').get('href')
            exhibit_url = start_museum_url + end_exhibit_url
            links.append(exhibit_url)

        legionofhonor_exhibits = zip(titles, dates, images, links)

        legionofhonor_df = pd.DataFrame(legionofhonor_exhibits,
                                        columns=['title', 'dates', 'image', 'link'])
        legionofhonor_df.insert(0, 'institution', 'legionofhonor')

        return legionofhonor_df

    # Function that scrapes OMCA Exhibit details
    def omca_scrape():
        # Request URL of OMCA Exhibits web page
        omca_page = requests.get("https://museumca.org/exhibitions")
        # Creates soup for reading HTML content easier
        omca_soup = BeautifulSoup(omca_page.content, 'html.parser')
        # Initialize empty lists to store data
        titles = []
        dates = []
        images = []
        links = []
        # Create variable as block of HTML which has info we need
        exhibition_div = omca_soup.find_all('li', class_='exhibit-list')
        # For loop to iterate through and extract data
        for container in exhibition_div:
            # Titles
            name = container.find('div', class_='list-omca-title-lrg').text
            titles.append(name)
            # Dates
            date = container.find('span', class_='field-name-field-display-date').text
            dates.append(date)
            # Links
            start_museum_url = 'https://museumca.org'
            end_exhibit_url = container.find('a').get('href')
            exhibit_url = start_museum_url + end_exhibit_url
            links.append(exhibit_url)

        # Images
        for image in links:
            image_page = requests.get(image)
            image_soup = BeautifulSoup(image_page.content, 'html.parser')
            image_div = image_soup.find('li', class_='flexslider-views-slideshow-main-frame-row')
            image_nice = image_div.find('img').get('src')
            images.append(image_nice)

        omca_exhibits = zip(titles, dates, images, links)

        omca_df = pd.DataFrame(omca_exhibits, columns=['title', 'dates', 'image', 'link'])
        omca_df.insert(0, 'institution', 'omca')

        return omca_df

    # GALLERY SCRAPING
    # Function that scrapes Legion of Honor Exhibit details
    def fraenkel_scrape():
        # Request URL of Legion of Honor Exhibits web page
        fraenkel_page = requests.get("https://fraenkelgallery.com/exhibitions")
        # Creates soup for reading HTML content easier
        fraenkel_soup = BeautifulSoup(fraenkel_page.content, 'html.parser')
        # Initialize empty lists to store data
        titles = []
        dates = []
        images = []
        links = []
        # Create variable as block of HTML which has info we need
        exhibition_div = fraenkel_soup.find('article', class_='exhibition_category-current')
        # Titles
        name = exhibition_div.find('h2', class_='entry-title').text
        titles.append(name)
        # Dates
        date = exhibition_div.find('div', class_='meta--exhibition-dates').text
        dates.append(date)
        # Images
        image_urls = exhibition_div.find('img').get('srcset')
        image = image_urls.split(" ")[0]
        images.append(image)
        # Links
        exhibit = exhibition_div.find('a').get('href')
        links.append(exhibit)

        fraenkel_exhibits = zip(titles, dates, images, links)

        fraenkel_df = pd.DataFrame(fraenkel_exhibits, columns=['title', 'dates', 'image', 'link'])
        fraenkel_df.insert(0, 'institution', 'fraenkel')

        return fraenkel_df

    def csv_exporter():
        bayareatracker_df = pd.concat([bampfa_scrape(), deyoung_scrape(), legionofhonor_scrape(), omca_scrape(),
                                       fraenkel_scrape()], axis=0)
        bayareatracker_df.to_csv(r'static/data/csv/bayareatracker.csv', index=False)

    return csv_exporter()


print(scrape_all())
