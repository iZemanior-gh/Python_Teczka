tags_input = input('Podaj zdnaie  ')

tags_list = tags_input.split(',')

cleaned_tags = [tag.strip() for tag in tags_list]

unique_tag = set(cleaned_tags)

print (f'Liczba wszystkich tagow: {len(cleaned_tags)}')
print (f'Liczba unikalnych tagow: {len(unique_tag)}')

sorted_unique_tag = sorted(unique_tag)

print('Unikalne tagi alfabetycnzie')

for tag in sorted_unique_tag:
    print(tag)