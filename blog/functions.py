# -*- coding: utf-8 -*-
import os, datetime, json, re, shutil, random
from bs4 import BeautifulSoup
from PIL import Image
from django.utils.encoding import uri_to_iri, iri_to_uri
from moviepy.editor import *

src_szs = [480, 800, 1366, 1600, 1920]

def validate_post_image(value):
    """ 
    Проверка что загружаемая картинка разрешенного типа
    принимает аргументом ссылку или путь к файлу
    """
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpeg','.jpg','.bmp', '.png', '.tiff', '.gif', '.webm']
    if not ext in valid_extensions:
    raise ValidationError(u'File not supported!')


def deleteThumb(text):
    """
    удаляем картинки при удалении поста 
    """
    img_links = re.findall\
        (r"/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<file>\S*)\
         -(?P<res>\d{3,4})\.(?P<ext>\S*)", str(text))
    img_path = []
    # ищем полные пути до картинок
    for img in img_links:
        img_path.append(uri_to_iri('/root/myblog/myblog/blog/static/media/\
                                                {}/{}/{}/{}{}.{}'
                                   .format(img[0], img[1], img[2], img[3], "-" +
                                                 img[4], img[5])))
        img_path.append(uri_to_iri('/root/myblog/myblog/blog/static/media/\
                                                {}/{}/{}/{}.{}'
                                   .format(img[0], img[1], img[2], img[3],
                                                                    img[5])))
    for img in img_path:
        if os.path.isfile(img):
            os.remove(img)


def srcsetThumb(data, post_id=None):
    """ 
    Конвертим картинки для главной страницы
    Принимает ссылку на файл и отдаёт готовый html код
    """
    thumb = BeautifulSoup("html5lib").new_tag("img")
    thumb['src'] = "/" + str(data)
    if post_id:
        soup = srcsets(thumb, False, post_id=post_id)
    else:
        soup = srcsets(thumb, False)
    soup.html.unwrap()
    soup.head.unwrap()
    soup.body.unwrap()
    image_url = soup.prettify()
    return str(image_url)


def findLink(text):
    """
    Парсим ссылку на файл
    """
    return re.search(r"/(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<file>\S*)\.(?P<ext>\w*)", str(text))


def findFile(link):
    """
    Парсим ссылку на файл и возвращаем полный путь до него
    """
    if link:
        return '/root/myblog/myblog/blog/static/media/{}/{}/{}/{}.{}'\
            .format(link.group("year"), link.group("month"), link.group("day"),
                                        link.group("file"), link.group("ext"))
    else:
        return ""


def saveImage(link, file, w, h=3500):
    """
    Сохраняем файл из ссылки, возвращает сслыку на картинку
    """

    file_out = '/root/myblog/myblog/blog/static/media/{}/{}/{}/{}-{}.{}'\
                        .format(link.group("year"), link.group("month"),
                        link.group("day"), uri_to_iri(link.group("file")),
                        w, link.group("ext"))

    link_out = '/media/{}/{}/{}/{}-{}.{}'\
            .format(link.group("year"), link.group("month"),
            link.group("day"), link.group("file"),
            w, link.group("ext"))
    img = Image.open(file)
    sz_tuple = (w, h)

    img.thumbnail(sz_tuple, Image.ANTIALIAS)
    img.save(file_out, subsampling=0, quality='keep')  # сохраняем
    return link_out


def srcsets(text, wrap_a, post_id=None):
    """
    Создаём srcsetы из картинок
    Принимает текст поста, оборачивать ли картинку в ссылку и опционально id поста
    Возвращает готовый html код
    """
    soup = BeautifulSoup(uri_to_iri(text), "html5lib")  # текст поста

    # ищем все картинки
    img_links_raw = soup.find_all("img")  
    print("***************************")
    print('img_links_raw ', str(img_links_raw))
    img_links = []
    for img in img_links_raw:  # фильтруем без srcset, ещё не обработанные
        if not img.has_attr('srcset'):
            img_links.append(img)

    print("***************************")
    print('img_links ', str(img_links))
    if len(img_links) != 0:
        for img in img_links:
            srcset = {}
            notgif = False

            # находим ссылку и файл и вых. файл
            del img['style']  # удаляем стиль

            link = findLink(iri_to_uri(img))
            print("***************************")
            print('link ', str(link))
            file = uri_to_iri(findFile(link))
            print("***************************")
            print('file ', str(file))
            original_pic = uri_to_iri('/media/{}/{}/{}/{}.{}'.\
                    format(link.group("year"), link.group("month"),
                    link.group("day"), link.group("file"),
                    link.group("ext")))

            print("***************************")
            print('original_pic ', str(original_pic))
            # сжимать пикчу! и удалять оригинальный файл

            if os.path.isfile(file):

                img['class'] = 'responsive-img post-image'
                ext = img['src'].split('.')[-1].lower()

                if ext == "gif" or ext == "webm":
                    notgif = False
                    clip = VideoFileClip(file)
                    w, h = clip.size
                else:
                    notgif = True
                    w, h = Image.open(file).size

                if notgif:
                    # если картинка больше нужного размера создаём миниатюру
                    for sz in reversed(src_szs):
                        if w > sz:
                            srcset[sz] = saveImage(link, file, sz)

                    if 1600 in srcset:
                        alt = srcset[1366]   # дефолт img src
                        # проверка пуст ли элемент
                        if 1920 not in srcset:
                            srcset[1920] = saveImage(link, file, 1920)

                    elif 1366 in srcset:
                        if 1600 not in srcset:
                            srcset[1600] = saveImage(link, file, 1600)

                        alt = srcset[1366]

                    elif 800 in srcset:
                        if 1366 not in srcset:
                            srcset[1366] = saveImage(link, file, 1366)

                        alt = srcset[1366]

                    elif 480 in srcset:
                        alt = original_pic
                        if 800 not in srcset:
                            srcset[800] = saveImage(link, file, 800)

                    else:
                        alt = original_pic
                        if 480 not in srcset:
                            srcset[480] = original_pic

                    src_str = ""
                    for src in srcset.keys():
                        src_str += srcset[src] + " " + str(src) + "w, "

                    src_str = src_str.rstrip(', ')
                    print("***************************")
                    print('src_str ', str(src_str))
                    img['srcset'] = src_str
                    img['src'] = alt
                    img['sizes'] = "60vw"

                else:  # конвертим гифки в webm
                    webm = BeautifulSoup("", "html5lib").new_tag("video")
                    webm['autoplay'] = ""
                    webm['loop'] = ""
                    webm['controls'] = ""
                    webm['style'] = "max-width: " + str(w) + "px;"
                    source = BeautifulSoup("", "html5lib").new_tag("source")
                    if ext == "webm":
                        source['src'] = "/media" + link.group()
                    else:
                        file_out = uri_to_iri("/root/myblog/myblog/blog/static/media/{}/{}/{}/{}-{}.webm"\
                        .format(link.group("year"), link.group("month"),
                            link.group("day"), link.group("file"), str(post_id)))
                        link_out = uri_to_iri('/media/{}/{}/{}/{}-{}.webm'\
                                .format(link.group("year"), link.group("month"),
                                link.group("day"), link.group("file"), str(post_id)))

                        clip = VideoFileClip(file)
                        video = CompositeVideoClip([clip])
                        video.write_videofile(file_out, codec='libvpx',
                                                audio=False, preset='superslow')
                        os.remove(file)

                        source['src'] = link_out
                    source['type'] = "video/webm"
                    webm.insert(0, source)
                    img.replaceWith(webm)

                if wrap_a and notgif:
                    a_tag = soup.new_tag("a")
                    # оборачиваем в ссылку на оригинал
                    a_tag['href'] = original_pic
                    a_tag['data-gallery'] = ""
                    img = img.wrap(a_tag)
    return soup


def stripMediaFromPath(file):
    """
    Удаляем "media/" из путей к файлам
    """
    if re.search(r"^/media/", file):
        path = file.split(os.sep)[2:]
        new_path=""
        for i in path:
            new_path = os.path.join(new_path, i)
        return uri_to_iri(new_path)
    else:
        return uri_to_iri(file)
