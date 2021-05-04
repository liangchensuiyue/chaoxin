#从selenium里面导入webdriver

import time
from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
import traceback

from selenium.webdriver.chrome.options import Options


class MyListener(AbstractEventListener):
    def after_click(self, element, driver):
        # print(element)
        super().after_click(element, driver)


# #指定chrom的驱动
# #执行到这里的时候Selenium会到指定的路径将chrome driver程序运行起来
# driver = webdriver.Chrome('D:/高东昇的宝库/PythonCode/chaoxingdatabase/chromedriver.exe')
# #driver = webdriver.Firefox()#这里是火狐的浏览器运行方法
#
# driver = EventFiringWebDriver(driver,MyListener())
#
#
#
# #get 方法 打开指定网址
# driver.get('https://i.mooc.chaoxing.com/space/index?t=1618399110710')
#
# driver.set_script_timeout(1000000)
#
# current_window = driver.current_window_handle
# origin_handler = None
# current_index = 0
# # driver.manage().timeouts().implicitlyWait(20000);
# # driver.implicitly_wait(2000)
# classlist = None
def get_script():
    with open('./event.js', encoding='utf-8') as f:
        js_script = f.read()
        return js_script

# def next(index):
    # global current_index
    # global classlist
    # # listframe = driver.find_element_by_id('content1')
    # # classlist = listframe.find_elements_by_tag_name('a')
    # try:
    #     print('............')
    #
    #     driver.refresh()
    #     driver.switch_to.parent_frame()
    #     driver.switch_to.parent_frame()
    #     driver.switch_to.parent_frame()
    #     listframe = driver.find_element_by_id('content1')
    #     classlist = listframe.find_elements_by_tag_name('a')
    #     print(len(classlist))
    #     print(classlist[index].get_attribute('title'))
    #     classlist[index].click()
    #     print('00000000000000')
    #     # driver.switch_to.window(origin_handler)
    #     # current_window = driver.current_window_handle
    #
    #     print(current_index)
    #     try:
    #         # driver.switch_to.parent_frame()
    #         # driver.switch_to.parent_frame()
    #         # driver.switch_to.parent_frame()
    #         # driver.switch_to.parent_frame()
    #         # listframe = driver.find_element_by_id('content1')
    #         # classlist = listframe.find_elements_by_tag_name('a')
    #         # current_window = driver.current_window_handle
    #         time.sleep(4)
    #
    #         driver.switch_to.frame('iframe')
    #
    #         print("by_tab_name")
    #         iframes = driver.find_elements_by_tag_name('iframe')
    #         iframelength = len(iframes)
    #         errnum = 0
    #         for i, frame in enumerate(iframes):
    #             try:
    #                 driver.switch_to.frame(frame)
    #
    #                 btn = driver.find_element_by_class_name('vjs-big-play-button')
    #                 btn.click()
    #                 video = driver.find_element_by_id('video_html5_api')
    #                 he = driver.execute_async_script(get_script(), video)
    #                 print(he)
    #             except Exception as e:
    #                 pass
    #
    #         # driver.switch_to.window(current_window)
    #         # listframe = driver.find_element_by_id('content1')
    #         # classlist = listframe.find_elements_by_tag_name('a')
    #
    #         for i, tag in enumerate(classlist):
    #             if i == current_index:
    #                 if i == len(classlist) - 1:
    #                     driver.close()
    #                     print('completed!')
    #                     exit(0)
    #                 else:
    #                     current_index = i + 1
    #                     next(i + 1)
    #                     driver.close()
    #                     print('completed!')
    #                     exit(0)
    #     except Exception as err:
    #         driver.switch_to.parent_frame()
    #         driver.switch_to.parent_frame()
    #         listframe = driver.find_element_by_id('content1')
    #         classlist = listframe.find_elements_by_tag_name('a')
    #         # if str(err).strip() == 'Message: iframe':
    #         #     driver.switch_to.default_content()
    #
    #         print(str(err).strip() )
    #         # print(traceback.print_exc())
    #         # listframe = driver.find_element_by_id('content1')
    #         # classlist = listframe.find_elements_by_tag_name('a')
    #         for i, tag in enumerate(classlist):
    #             if i == current_index:
    #                 if i == len(classlist) - 1:
    #                     driver.close()
    #                     print('completed!')
    #                     exit(0)
    #                 else:
    #                     current_index = i + 1
    #                     next(i + 1)
    #                     driver.close()
    #                     print('completed!')
    #                     exit(0)
    # except Exception as err:
    #     print(err)
    #     driver.close()

# #选择网页元素
# uname_input = driver.find_element_by_id('unameId')
# password_input = driver.find_element_by_id('passwordId')
# verify_input = driver.find_element_by_id('numcode')
#
# #输入字符
# uname_input.send_keys('15581258944')
# password_input.send_keys('abc1497367496')
# verify_code = input('输入验证码: ')
#
# verify_input.send_keys(verify_code)
#
#
#
# #找到提交
# login_button = driver.find_element_by_class_name('zl_btn_right')
# login_button.click()

# verify_input = driver.find_element_by_id('mainphoto')
# verify_input.click()


# a=input('press any button')
# # driver.refresh()
# all_window=driver.window_handles
# for window in all_window:
#     if window != current_window:
#         driver.switch_to.window(window)
#         current_window = driver.current_window_handle
#
#
#
# origin_handler = current_window




# # 获取目录列表
# listframe = driver.find_element_by_id('content1')
# classlist = listframe.find_elements_by_tag_name('a')
#
# title = driver.find_element_by_tag_name('h1')
# print(title.text)
# print('start..............')
# for i, tag in enumerate(classlist):
#     if str(classlist[i].get_attribute('title')).strip() == title.text:
#         print(i)
#         current_index = i
#         break
#
# try:
#     # listframe = driver.find_element_by_id('content1')
#     # classlist = listframe.find_elements_by_tag_name('a')
#     driver.switch_to.frame('iframe')
#     iframe2 = driver.find_element_by_tag_name('iframe')
#     driver.switch_to.frame(iframe2)
#
#     # 播放视频
#     # btn = driver.find_element_by_class_name('vjs-big-play-button')
#     # btn.click()
#
#     video = driver.find_element_by_id('video_html5_api')
#     he = driver.execute_async_script(get_script(), video)
#     print(he)
#
#     for i, tag in enumerate(classlist):
#         print(i, tag.get_attribute('title'))
#         if i == current_index:
#             if i == len(classlist) - 1:
#                 print('completed!')
#                 driver.close()
#                 exit(0)
#             else:
#                 print(i, '+++++++++++++++++')
#                 current_index = i + 1
#                 next(i+1)
#                 driver.close()
#                 break
# except Exception:
#     driver.switch_to.default_content()
#     # listframe = driver.find_element_by_id('content1')
#     # classlist = listframe.find_elements_by_tag_name('a')
#     for i, tag in enumerate(classlist):
#         print(i, tag.get_attribute('title'))
#         if  i == current_index:
#             if i == len(classlist) - 1:
#                 print('completed!')
#                 driver.close()
#                 exit(0)
#             else:
#                 print(i, '+++++++++++++++++')
#                 current_index = i + 1
#                 next(i + 1)
#                 # driver.close()
#                 break


class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self):
        super()
        options = Options()  # 网上找到 你可以试试
        options.binary_location = "./Google/Chrome/Application/chrome.exe"  # 这里是你指定浏览器的路径
        # 指定chrom的驱动
        # 执行到这里的时候Selenium会到指定的路径将chrome driver程序运行起来
        self.driver = webdriver.Chrome('./chromedriver.exe',chrome_options=options)
        # driver = webdriver.Firefox()#这里是火狐的浏览器运行方法

        # driver = EventFiringWebDriver(driver, MyListener())

        # get 方法 打开指定网址
        self.driver.get('https://i.mooc.chaoxing.com/space/index?t=1618399110710')

        self.driver.set_script_timeout(1000000)
    def login(self,uname,pd,code):
        self.username=uname
        self.password=pd
        self.code=code


        self.current_window = self.driver.current_window_handle
        self.origin_handler = None
        self.current_index = 0
        # driver.manage().timeouts().implicitlyWait(20000);
        # driver.implicitly_wait(2000)
        self.classlist = None


        # 选择网页元素
        uname_input = self.driver.find_element_by_id('unameId')
        password_input = self.driver.find_element_by_id('passwordId')
        verify_input = self.driver.find_element_by_id('numcode')

        # 输入字符
        uname_input.clear()
        password_input.clear()
        uname_input.send_keys(self.username)
        password_input.send_keys(self.password)

        verify_input.send_keys(self.code)
        title = self.driver.title
        # 找到提交
        login_button = self.driver.find_element_by_class_name('zl_btn_right')
        login_button.click()
        time.sleep(2)


    def stop(self):
        try:
            self.driver.close()
        except Exception:
            pass
    def start(self):
        self.origin_handler = None
        self.current_index = 0
        # driver.manage().timeouts().implicitlyWait(20000);
        # driver.implicitly_wait(2000)
        self.classlist = None
        self.current_video = None
        all_window=self.driver.window_handles
        for window in all_window:
             if window != self.current_window:
                self.driver.switch_to.window(window)
                self.current_window = self.driver.current_window_handle


        self.driver.refresh()
        time.sleep(3)
        # 获取目录列表
        listframe = self.driver.find_element_by_id('content1')
        self.classlist = listframe.find_elements_by_tag_name('a')

        title = self.driver.find_element_by_tag_name('h1')
        print(title.text)
        print('start..............')
        for i, tag in enumerate(self.classlist):
            if str(self.classlist[i].get_attribute('title')).strip() == title.text:
                print(i)
                self.current_index = i
                break

        try:
            self.Next(self.current_index)
        except Exception:
            return '发生了点错误'

    def mute(self):
        try:
            video = self.driver.find_element_by_id('video_html5_api')
            print('start mute')
            self.driver.execute_script('arguments[0].muted = true;',video)
            print('end mute')
        except Exception as e:

            print(e)

    def playSpeed(self, speed):
        try:
            self.driver.execute_script("arguments[0].playbackRate=arguments[1]",self.current_video,speed)
        except Exception:
            pass
    def play(self):
        try:
            print("Play start")

            video = self.driver.find_element_by_id('video_html5_api')

            print("Play middle")
            self.driver.execute_async_script("return arguments[0].play()",video)
            print("Play end")

        except Exception:
            pass
    def Next(self, index):
        # listframe = self.driver.find_element_by_id('content1')
        # classlist = listframe.find_elements_by_tag_name('a')
        try:
            print('............')

            self.driver.refresh()
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.parent_frame()
            self.driver.switch_to.parent_frame()
            listframe = self.driver.find_element_by_id('content1')
            self.classlist = listframe.find_elements_by_tag_name('a')
            print(len(self.classlist))
            print(self.classlist[index].get_attribute('title'))
            self.classlist[index].click()
            print('00000000000000')
            # driver.switch_to.window(origin_handler)
            # current_window = driver.current_window_handle
            time.sleep(3)
            self.tags = self.driver.find_elements_by_css_selector(".tabtags span")
            print(len(self.tags))
            for tag in self.tags:
                print(tag.text)
            print(self.current_index)
            # if len(self.tags) > 0:

            try:
                # iframelength = len(iframes)
                # errnum = 0
                current_tag_index = 0
                if len(self.tags) >0:

                    for j in range(len(self.tags)):
                        self.driver.refresh()
                        self.driver.switch_to.parent_frame()
                        self.driver.switch_to.parent_frame()
                        self.driver.switch_to.parent_frame()
                        listframe = self.driver.find_element_by_id('content1')
                        self.classlist = listframe.find_elements_by_tag_name('a')
                        self.classlist[index].click()
                        time.sleep(3)
                        self.tags = self.driver.find_elements_by_css_selector(".tabtags span")

                        print("tag click", self.tags[j].text)
                        self.tags[j].click()
                        time.sleep(4)
                        self.driver.switch_to.frame('iframe')
                        iframes = self.driver.find_elements_by_tag_name('iframe')
                        for i, frame in enumerate(iframes):
                            try:
                                self.driver.switch_to.frame(frame)

                                btn = self.driver.find_element_by_class_name('vjs-big-play-button')
                                btn.click()
                                video = self.driver.find_element_by_id('video_html5_api')
                                self.current_video = video
                                he = self.driver.execute_async_script(get_script(), video)
                                print(he)
                            except Exception as e:
                                print(e,'400 400')
                                pass
                        print('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
                else:
                    time.sleep(4)
                    self.driver.switch_to.frame('iframe')
                    iframes = self.driver.find_elements_by_tag_name('iframe')
                    for i, frame in enumerate(iframes):
                        try:
                            self.driver.switch_to.frame(frame)

                            btn = self.driver.find_element_by_class_name('vjs-big-play-button')
                            btn.click()
                            video = self.driver.find_element_by_id('video_html5_api')
                            self.current_video = video
                            he = self.driver.execute_async_script(get_script(), video)
                            print(he)
                        except Exception as e:
                            pass

                # driver.switch_to.window(current_window)
                # listframe = driver.find_element_by_id('content1')
                # classlist = listframe.find_elements_by_tag_name('a')

                for i, tag in enumerate(self.classlist):
                    if i == self.current_index:
                        if i == len(self.classlist) - 1:
                            self.driver.close()
                            print('completed!')
                            # exit(0)
                        else:
                            self.current_index = i + 1
                            self.Next(i + 1)
                            self.driver.close()
                            print('completed!')
                            # exit(0)
            except Exception as err:
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.parent_frame()
                listframe = self.driver.find_element_by_id('content1')
                self.classlist = listframe.find_elements_by_tag_name('a')
                # if str(err).strip() == 'Message: iframe':
                #     driver.switch_to.default_content()

                print(traceback.print_exc())
                # print(traceback.print_exc())
                # listframe = driver.find_element_by_id('content1')
                # classlist = listframe.find_elements_by_tag_name('a')
                for i, tag in enumerate(self.classlist):
                    if i == self.current_index:
                        if i == len(self.classlist) - 1:
                            self.driver.close()
                            print('completed!')
                            exit(0)
                        else:
                            self.current_index = i + 1
                            self.Next(i + 1)
                            self.driver.close()
                            # print('completed!')
                            break
                            # exit(0)
        except Exception as err:
            print(err)
            self.driver.close()











