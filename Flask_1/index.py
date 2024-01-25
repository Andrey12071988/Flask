# Задание No9
# 📌 Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна(шапка, меню, подвал), и
# дочерние шаблоны для страниц категорий товаров и отдельных товаров.
# 📌 Например, создать страницы "Одежда", "Обувь" и "Куртка", используя базовый шаблон.

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def my_shop():
    return render_template('base.html')


@app.route('/clothes/')
def clothes():
    clothes = {
        'name': 'Товар',
        'size': 'Размер',
        'amount': 'В наличии'
    }

    clothes_list = [
        {
            'name': 'Рубашка',
            'size': 'S, M, L, XL, XXL',
            'amount': 34
        },
        {
            'name': 'Юбка',
            'size': 'S, M, L, XXL',
            'amount': 5
        },
        {
            'name': 'Брюки',
            'size': 'XS, S, L, XXXL',
            'amount': 12
        }
    ]
    return render_template('clothes.html', **clothes, clothes_list=clothes_list)


@app.route('/shoes/')
def shoes():
    shoes = {
        'name': 'Товар',
        'size': 'Размер',
        'amount': 'В наличии'
    }

    shoes_list = [
        {
            'name': 'Кроссовки',
            'size': '20-36',
            'amount': 15
        },
        {
            'name': 'Ботинки',
            'size': '36-44',
            'amount': 5
        }
    ]
    return render_template('shoes.html', **shoes, shoes_list=shoes_list)


@app.route('/accessories/')
def accessories():
    accessories = {
        'name': 'Товар',
        'size': 'Размерный ряд',
        'amount': 'В наличии'
    }

    accessories_list = [
        {
            'name': 'Шапка',
            'size': '46-56',
            'amount': 8
        },
        {
            'name': 'Перчатки',
            'size': '5-8',
            'amount': 10
        }
    ]
    return render_template('accessories.html', **accessories,
                           accessories_list=accessories_list)


if __name__ == '__main__':
    app.run(debug=True)
