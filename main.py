import json

class Raf9:
    def __init__(self):
        self.ingredients = ['lemon', 'mint', 'ice', 'soda', 'orange', 'tomato']
        self.get_cocktails_from_db()

    def __call__(self, *args, **kwargs):
        while True:
            self.__help_text()
            command = input('Введите команду: ')
            if command == '0':
                print('Всего доброго, приходите еще!')
                break
            elif command == '1':
                current_ing = self.choose_ingredients()
                chose_cocktail = self.find_cocktail(current_ing)
                if chose_cocktail is None:
                    self.save_cocktail(current_ing)
                else:
                    print(f'Вы выбрали {chose_cocktail} коктейль')
            else:
                print('Неверная команда')

    def __help_text(self):
        print('Доступны команды:')
        print('1: выбрать ингредиенты')
        print('0: выход')

    def save_cocktail(self, current_ings):
        self.cocktails.append({
            'name': 'unnamed',
            'ingredients': current_ings
        })

        with open('cocktails.json', 'w') as json_file:
            json.dump(self.cocktails, json_file)
    def get_cocktails_from_db(self):
        with open('cocktails.json', 'r') as json_file:
            self.cocktails = json.load(json_file)

    def find_cocktail(self, current_ings):
        for c in self.cocktails:
            print(c.get('ingredients'))
            print(current_ings)
#            this_cocktail = False
            if c.get('ingredients') == current_ings:
#               this_cocktail = True
                return c.get('name')
        return None

    def choose_ingredients(self):
        choosed_ings = []
        print('Список ингредиентов: ')
        i = 0
        for ing in self.ingredients:
            i += 1
            print(f'{i}. {ing}')
        print('0 - для выхода')
        while True:
            command = input('Введите команду: ')
            if command == '0':
                return choosed_ings
            else:
                if command.isdigit():
                    number = int(command)
                    if number >= len(self.ingredients):
                        print('Такого ингредиента в списке нет')
                    else:
                        choosed_ings.append(self.ingredients[number-1])
                else:
                    print('Введите НОМЕР ингредиента')

if __name__ == '__main__':
    raf9 = Raf9()
    raf9()

