
volume = 1.44 #объем дискеты
pages = 100 #количество страниц в книге
lines = 50 #число строк на странице
symbol = 25 #количество символов в строке
bite_for_symbol = 4 #количество байтов для хранения одного символа

volume_1 = volume * 1024 * 1024 #объем дискеты в байтах
volume_1 = round(volume_1)
bite_for_line = symbol * bite_for_symbol #количество байтов на строку
bite_for_page = bite_for_line * lines #количество байтов на страницу
bite_for_book = bite_for_page * pages #количество байтов на книгу

count_of_books = volume_1 // bite_for_book
print("Количество книг, помещающихся на дискету:", count_of_books)