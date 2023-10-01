import tkinter as tk
from tkinter import messagebox
from tkinter import font
from .update_link import *
from .write_to_world import *

waiting_text = "please wait, under processing..."

def search_main_article_link(english_link):
    vietnamese_link = find_vietnamese_link_1(english_link)
    return vietnamese_link


def search_related_article_link(english_link):
    result_text = []
    result_text.append("Related reports:")
    result_text.append("Bài liên quan:")

    if english_link:
        vietnam_link, english_link_list = find_vietnamese_link_2(english_link)
        if english_link_list:
            for i in range(len(english_link_list)):
                # Kiểm tra xem link có chứa "en.minghui.org" hay không
                if "en.minghui.org" in english_link_list[i]:
                    result_text.append(get_en_article_title(english_link_list[i]))
                    result_text.append(vietnam_link[i])
            result_text_final = "\n".join(result_text)
        else:
            result_text_final = "Have no related link in article"
    else:
        english_text, vietnam_link, english_link = find_vietnamese_link(english_link)
        if english_link:
            for i in range(len(english_link)):
                result_text.append(get_en_article_title(english_link[i]))
                result_text.append(vietnam_link[i])
            result_text_final = "\n".join(result_text)
        else:
            result_text_final = "Have no related link in article"

    return result_text_final

def update_new_link():
    get_new_link_vn(article_url_GCT)
    get_new_link_en(file_new_gct_vn)
    add_link_to_csv(file_new_gct_en, file_new_gct_vn)

    get_new_link_vn(article_url_tdth)
    get_new_link_en(file_new_gct_vn)
    add_link_to_csv(file_new_gct_en, file_new_gct_vn)

    get_new_link_vn(article_url_new)
    get_new_link_en(file_new_gct_vn)
    add_link_to_csv(file_new_gct_en, file_new_gct_vn)
    text = "Update Successful"
    return text


def create_docx_file(url):
    english_artical, link_en, link_cn = write_en_article_to_doc(url)
    english_text = "\n".join(english_artical)
    return english_text
def Auto_Translate(url):
    english_artical = read_paragraph_in_word(url)
    english_text = "\n".join(english_artical)

    return english_text

def text_execute(english, vietnam, in_text):
    count = []
    english_list =  tokenize_sentences_with_name_prefix(english)
    vietnamse_list = tokenize_sentences_with_name_prefix(vietnam)
    for i in range(len(english_list)):
        check_point = False
        for j in range(len(in_text)):
            if in_text[j] in english_list[i]:
                check_point = True
                break
        if check_point:
            count.append(i)
    return english_list, vietnamse_list, count

def update_link():
    update_text = update_new_link()


def search_main_link(user_input):
        result = search_main_article_link(user_input)
        return result


def search_related_link(user_input):
    # Xóa nội dung hiển thị kết quả
    pattern = r"^(http:|https:).*\.html$"

    if not user_input:
        return "Please input text"
    elif not re.match(pattern, user_input):
            return "Please check url"
    else:
        result = search_related_article_link(user_input)
        return result

def article_content(user_input):
    # Xóa nội dung hiển thị kết quả
    pattern = r"^(http:|https:).*\.html$"
    if not user_input:
        return "Please input text"
    elif not re.match(pattern, user_input):
            return "Please check url"
    else:
        result = create_docx_file(user_input)
        return result

def translation(user_input):
    # Xóa nội dung hiển thị kết quả
    pattern = r"^(http:|https:).*\.html$"
    if not user_input:
        return "Please input text"
    elif not re.match(pattern, user_input):
            return "Please check url"
    else:
        result = Auto_Translate(user_input)
        return result


def searc_kv(user_input):
    result = []
    if not user_input:
        return "Please input text"
    else:
        english_text_in, vietname_text_in, in_text = find_translation(user_input)
        if not english_text_in:
            return "Can not found"

        english_text, vietname_text, list = text_execute(english_text_in[0], vietname_text_in[0], in_text)
        for i in range(len(english_text)):
            result.append(english_text[i])
        for j in range(len(vietname_text)):
            result.append(vietname_text[i])
    return result

def search_sentence(user_input):
    if not user_input:
        return "Please input text"
    else:
        search_result = find_sentence(user_input)
        if not search_result:
            return "Can not found"
        result = "\n".join(search_result)
    return result

