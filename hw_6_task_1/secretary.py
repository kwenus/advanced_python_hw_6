all_documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
    {"type": "passport", "number": "54513", "name": "Казимир Малевич"},
    {"type": "driver license", "number": "48765-av", "name": "Пабло Пикассо"}]

all_directories = {'1': ['2207 876234','5455 028765'],
     '2': ['10006'],
     '3': ['54513'],
     '4': [],
     '5': ['48765-av',  '11-2']}


# функции для записи и распределения документов по полкам

# 1) получить имя по номеру документа
def get_name(documents, doc_number):
    for el in documents:
        if el.get('number') == doc_number:
            return el.get('name')
    return 'Документ не найден'

# 2) получить номер полки по номеру документа
def get_directory(directories, doc_number):
    for el in directories.items():
        if doc_number in el[1]:
            return el[0]
    return 'Полки с таким документом не найдено'

# 3) добавить документы на полку
def add_docs(documents, directories, document_type, number, name, shelf_number):
    new_dict = {
        "type": document_type,
        "number": number,
        "name": name,
    }
    documents.append(new_dict)
    if str(shelf_number) in directories:
        directories[str(shelf_number)].append(number)
    else:
        directories[str(shelf_number)] = [number]


if __name__ == '__main__':

    print(get_name(all_documents, "10006"))
    print(get_directory(all_directories,"11-2"))
    add_docs(all_documents, all_directories, 'international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory(all_directories, "311 020203"))
    print(get_name(all_documents, "311 020203"))
    print(get_directory(all_directories, "311 020204"))
