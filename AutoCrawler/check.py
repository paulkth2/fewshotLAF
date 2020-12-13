import main
import glob
import PIL.Image
import os

def crawling(keyword):
    _skip = False
    _threads = 4
    _google = True
    _naver = False
    _full = True
    _face = False
    _limit = 10
    _no_gui = _full

    _keyword = keyword
    print('Options - skip:{}, threads:{}, google:{}, naver:{}, full_resolution:{}, face:{}, no_gui:{}, limit:{}, keyword:{}'
          .format(_skip, _threads, _google, _naver, _full, _face, _no_gui, _limit, _keyword))

    crawler = main.AutoCrawler(skip_already_exist=_skip, n_threads=_threads,
                          do_google=_google, do_naver=_naver, full_resolution=_full,
                          face=_face, no_gui=_no_gui, limit=_limit, keyword=_keyword)
    crawler.do_crawling()
    resize(keyword, (500, 500))



def resize(folder, size):
    path = 'download/' + folder
    images = glob.glob(path + "/*.jpg")
    for image in images:
        img = PIL.Image.open(image)
        img1 = img.resize(size)
        img1.save(image)
    
