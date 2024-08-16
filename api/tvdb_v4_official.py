#!/usr/bin/env python3


import os
from dotenv import load_dotenv

import tvdb_v4_official

load_dotenv()

my_api_key = os.getenv('my_api_key')
tvdb = tvdb_v4_official.TVDB(my_api_key)


# На странице Discover - Awards получить перечень названий
# всех премий, которые учитываются в базе
def get_awards():
    awards_list = tvdb.get_all_awards()
    print('Перечень названий всех премий:')
    for award in awards_list:
        print(award['name'])


# На странице Discover - Official Lists получить перечень
# названий 10-ти последних публикаций
def get_latest_publications():
    publications_list = tvdb.get_all_lists()
    print('Перечень названий 10-ти последних публикаций:')
    for publications in publications_list[:10]:
        print(publications['name'])


# На странице Discover - Companies получить перечень из 15-ти
# названий компаний, связанных с TheTVDB.com
def get_companies():
    companies_list = tvdb.get_all_companies()
    print('Перечень из 15-ти названий компаний, связанных с TheTVDB.com:')
    for companies in companies_list[:15]:
        print(companies['name'])


def main():
    get_awards()
    print('\n')
    get_latest_publications()
    print('\n')
    get_companies()


if __name__ == '__main__':
    main()
