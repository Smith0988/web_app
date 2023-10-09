from .update_link import *
from .write_to_world import *

waiting_text = "please wait, under processing..."



def update_new_link():


    result = []
    get_new_link_vn(article_url_GCT)
    get_new_link_en(file_new_gct_vn)
    add_link_to_csv(file_new_gct_en, file_new_gct_vn)

    get_new_link_vn(article_url_tdth)
    get_new_link_en(file_new_gct_vn)
    add_link_to_csv(file_new_gct_en, file_new_gct_vn)

    get_new_link_vn(article_url_new)
    get_new_link_en(file_new_gct_vn)
    add_link_to_csv(file_new_gct_en, file_new_gct_vn)

    get_new_link_vn(article_url_ddbl)
    get_new_link_en(file_new_gct_vn)
    add_link_to_csv(file_new_gct_en, file_new_gct_vn)

    get_new_link_vn(article_url_tguh)
    get_new_link_en(file_new_gct_vn)
    add_link_to_csv(file_new_gct_en, file_new_gct_vn)

    result.append("Update Successful")

    return result



def search_main_article_link(english_link):
    result_link = []
    vietnamese_link = find_vietnamese_link_1(english_link)
    if "Can not" in vietnamese_link:
        result_link.append(vietnamese_link)
        return result_link
    else:
        result_link.append(get_en_article_title(english_link))
        result_link.append(english_link)
        result_link.append(get_vn_article_title(vietnamese_link))
        result_link.append(vietnamese_link)
        #result_link = "\n".join(result_link)
        return result_link


def search_related_article_link(english_link):
    result_text = []
    # Xóa nội dung hiển thị kết quả
    pattern = r"^(http:|https:).*\.html$"
    if not re.match(pattern, english_link):
            result_text.append("Please check url")
            return result_text

    english_text, vietnam_link, english_link = find_vietnamese_link(english_link)
    if english_link:
        result_text.append("Related reports:")
        result_text.append("Related reports:")
        result_text.append("Bài liên quan:")
        result_text.append("Bài liên quan:")
        for i in range(len(english_link)):
            if "en.minghui.org" in english_link[i]:
                result_text.append(get_en_article_title(english_link[i]))
                result_text.append(english_link[i])
                if "vn.minghui.org" in vietnam_link[i]:
                    result_text.append(get_vn_article_title(vietnam_link[i]))
                    result_text.append(vietnam_link[i])
                else:
                    result_text.append("Can not found Vietnamese Link")
                    result_text.append(vietnam_link[i])
                #result_text.append("      ")
        #result_text_final = "\n".join(result_text)
    else:
        result_text.append("Have no related link in article")

    return result_text

def search_all_article_link(english_link):
    result_text = []
    # Xóa nội dung hiển thị kết quả
    pattern = r"^(http:|https:).*\.html$"
    if not re.match(pattern, english_link):
            result_text.append("Please check url")
            return result_text

    vietnam_link, english_link_list = find_vietnamese_link_2(english_link)
    if english_link_list:
        result_text.append("Các link có trong báo cáo:")
        result_text.append("Các link có trong báo cáo:")
        for i in range(len(english_link_list)):
            if "en.minghui.org" in english_link_list[i]:
                result_text.append(get_en_article_title(english_link_list[i]))
                result_text.append(english_link_list[i])
                if "vn.minghui.org" in vietnam_link[i]:
                    result_text.append(get_vn_article_title(vietnam_link[i]))
                    result_text.append(vietnam_link[i])
                else:
                    result_text.append("Can not found Vietnamese Link")
                    result_text.append(vietnam_link[i])
                #result_text.append("      ")
        #result_text_final = "\n".join(result_text)
    else:
        result_text.append("Have no related link in article")
    return result_text



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
        result.append("Please input search text:")
        return result
    else:
        english_text_in, vietname_text_in, in_text, vietname_link = find_translation(user_input)
        #if not vietname_link:
            #return "Can not found Vietnam Linkeqrntr"
        if not english_text_in:
            result.append("Can not found")
            return result
        result.append(english_text_in)
        result.append("=================================================================================")
        result.append(vietname_text_in)
        result.append("=================================================================================")
        for i in range(len(vietname_link)):
            result.append(vietname_link[i])
    return result

def search_sentence(user_input):
    result = []
    if not user_input:
        result.append("Please input text")
        return result
    else:
        search_result = find_sentence(user_input)
        if not search_result:
            result.append("Can not found")
            return result
        result = search_result
    return result

