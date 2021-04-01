import json

with open('tag_files.json') as f:
    files = json.load(f)

def show_tags():
   i = 0
   for file in files['file_names']:
      print(i, " ", file['name'])
      i = i + 1

def get_tag_file(tag):
    newFileName = tag.replace(" ", "_")
    newFileName = newFileName.lower()
    newFileName = newFileName + ".json"
    return newFileName

def add_tag(newTag):
    newFileName = get_tag_file(newTag)

    for tags in files['file_names']:
        if tags['path'] == newFileName:
            print(tag, "already exists")
            return

    newPair = {
            "name" : newTag,
            "path" : newFileName
            }

    files['file_names'].append(newPair)

    newJSON = {
            "name" : newTag,
            "links" : []
            }

    with open(newFileName, 'x') as file:
        file.write(json.dumps(newJSON, indent=2))

def save():
    with open('tag_files.json', 'w') as f:
        f.write(json.dumps(files, indent=4))

def assign_tag(tag, title, fileName):
    fileName = "../stories/" + fileName
    newPair = {
            "name" : title,
            "link" : fileName
            }

    tagged = 0

    with open(get_tag_file(tag)) as file:
        tagged = json.load(file);

    for pair in tagged['links']:
        if pair['link'] == fileName:
            print(title, "is already tagged with", tag)
            return

    tagged['links'].append(newPair)

    with open(get_tag_file(tag), 'w') as file:
        file.write(json.dumps(tagged, indent=2))

def show_options():
    print("o - Show options")
    print("s - Show Tags")
    print("n - Make New Tag")
    print("a - Assign tag to post")
    print("r - Remove post from tag")
    print("q - Quit")


loop = True
show_options()

while loop:
    next_action = input("> ")
    if next_action == 'o':
        show_options()
    elif next_action == 's':
        show_tags()
    elif next_action == 'n':
        newTag = input("New tag name: ")
        add_tag(newTag)
        save()
    elif next_action == 'a':
        tag = input("Tag: ")
        title = input("Title: ")
        path = input("File name: ")
        assign_tag(tag, title, path)
    elif next_action == 'r':
        print("Feature coming soon")
    elif next_action == 'q':
        save()
        loop = False
