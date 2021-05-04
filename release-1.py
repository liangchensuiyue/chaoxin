#从selenium里面导入webdriver

import time
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import traceback




class MyListener(AbstractEventListener):
    def after_click(self, element, driver):
        # print(element)
        super().after_click(element, driver)


#指定chrom的驱动
#执行到这里的时候Selenium会到指定的路径将chrome driver程序运行起来
driver = webdriver.Chrome('./tools/chromedriver.exe')
#driver = webdriver.Firefox()#这里是火狐的浏览器运行方法

driver = EventFiringWebDriver(driver,MyListener())



#get 方法 打开指定网址
driver.get('https://i.mooc.chaoxing.com/space/index?t=1618399110710')

driver.set_script_timeout(1000000)

current_window = driver.current_window_handle
origin_handler = None
current_index = 0
# driver.manage().timeouts().implicitlyWait(20000);
# driver.implicitly_wait(2000)
classlist = None
def get_script():
    with open('./event.js', encoding='utf-8') as f:
        js_script = f.read()
        return js_script

def next(index):
    global current_index
    global classlist
    # listframe = driver.find_element_by_id('content1')
    # classlist = listframe.find_elements_by_tag_name('a')
    try:

        driver.refresh()
        driver.switch_to.parent_frame()
        driver.switch_to.parent_frame()
        driver.switch_to.parent_frame()
        listframe = driver.find_element_by_id('content1')
        classlist = listframe.find_elements_by_tag_name('a')
        classlist[index].click()
        # driver.switch_to.window(origin_handler)
        # current_window = driver.current_window_handle

        try:
            # driver.switch_to.parent_frame()
            # driver.switch_to.parent_frame()
            # driver.switch_to.parent_frame()
            # driver.switch_to.parent_frame()
            # listframe = driver.find_element_by_id('content1')
            # classlist = listframe.find_elements_by_tag_name('a')
            # current_window = driver.current_window_handle
            time.sleep(4)

            driver.switch_to.frame('iframe')

            iframes = driver.find_elements_by_tag_name('iframe')
            iframelength = len(iframes)
            errnum = 0
            for i, frame in enumerate(iframes):
                try:
                    driver.switch_to.frame(frame)

                    btn = driver.find_element_by_class_name('vjs-big-play-button')
                    btn.click()
                    video = driver.find_element_by_id('video_html5_api')
                    he = driver.execute_async_script(get_script(), video)
                except Exception as e:
                    pass

            # driver.switch_to.window(current_window)
            # listframe = driver.find_element_by_id('content1')
            # classlist = listframe.find_elements_by_tag_name('a')

            for i, tag in enumerate(classlist):
                if i == current_index:
                    if i == len(classlist) - 1:
                        driver.close()
                        print('completed!')
                        exit(0)
                    else:
                        current_index = i + 1
                        next(i + 1)
                        driver.close()
                        print('completed!')
                        exit(0)
        except Exception as err:
            driver.switch_to.parent_frame()
            driver.switch_to.parent_frame()
            listframe = driver.find_element_by_id('content1')
            classlist = listframe.find_elements_by_tag_name('a')
            # if str(err).strip() == 'Message: iframe':
            #     driver.switch_to.default_content()

            # print(traceback.print_exc())
            # listframe = driver.find_element_by_id('content1')
            # classlist = listframe.find_elements_by_tag_name('a')
            for i, tag in enumerate(classlist):
                if i == current_index:
                    if i == len(classlist) - 1:
                        driver.close()
                        print('completed!')
                        exit(0)
                    else:
                        current_index = i + 1
                        next(i + 1)
                        driver.close()
                        print('completed!')
                        exit(0)
    except Exception as err:
        driver.close()

#选择网页元素
uname_input = driver.find_element_by_id('unameId')
password_input = driver.find_element_by_id('passwordId')
verify_input = driver.find_element_by_id('numcode')

#输入字符
uname_input.send_keys('15581258944')
password_input.send_keys('abc1497367496')
verify_code = input('输入验证码: ')

verify_input.send_keys(verify_code)



#找到提交
login_button = driver.find_element_by_class_name('zl_btn_right')
login_button.click()

# verify_input = driver.find_element_by_id('mainphoto')
# verify_input.click()


a=input('press any button')
# driver.refresh()
all_window=driver.window_handles
for window in all_window:
    if window != current_window:
        driver.switch_to.window(window)
        current_window = driver.current_window_handle



origin_handler = current_window




# 获取目录列表
listframe = driver.find_element_by_id('content1')
classlist = listframe.find_elements_by_tag_name('a')

title = driver.find_element_by_tag_name('h1')
for i, tag in enumerate(classlist):
    if str(classlist[i].get_attribute('title')).strip() == title.text:
        current_index = i
        break

try:
    # listframe = driver.find_element_by_id('content1')
    # classlist = listframe.find_elements_by_tag_name('a')
    driver.switch_to.frame('iframe')
    iframe2 = driver.find_element_by_tag_name('iframe')
    driver.switch_to.frame(iframe2)

    # 播放视频
    # btn = driver.find_element_by_class_name('vjs-big-play-button')
    # btn.click()

    video = driver.find_element_by_id('video_html5_api')
    he = driver.execute_async_script(get_script(), video)

    for i, tag in enumerate(classlist):
        if i == current_index:
            if i == len(classlist) - 1:
                print('completed!')
                driver.close()
                exit(0)
            else:
                current_index = i + 1
                next(i+1)
                driver.close()
                break
except Exception:
    driver.switch_to.default_content()
    # listframe = driver.find_element_by_id('content1')
    # classlist = listframe.find_elements_by_tag_name('a')
    for i, tag in enumerate(classlist):
        if  i == current_index:
            if i == len(classlist) - 1:
                print('completed!')
                driver.close()
                exit(0)
            else:
                current_index = i + 1
                next(i + 1)
                # driver.close()
                break
















