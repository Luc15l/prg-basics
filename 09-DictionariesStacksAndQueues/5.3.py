translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
słowo = input("word in english: ")
for english, polish in translations.items():
    if słowo in  english:
        print(translations[słowo])