from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

URL = "http://www.pbc.gov.cn/redianzhuanti/118742/118714/119413/index.html"
chrome_driver_path = '/Users/zhenziyang/Downloads/chromedriver-mac-arm64/chromedriver'  # 你的chromedriver路径

options = webdriver.ChromeOptions()
options.add_argument("--headless")  # 在后台运行（调试时建议先注释掉）

service = Service(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=service, options=options)

driver.get(URL)

# 等待页面加载
driver.implicitly_wait(4)

# 找到链接
links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/jinrongshichangsi/147160/147289/']")

# 存储主窗口的句柄（窗口ID）
main_window_handle = driver.current_window_handle

# 存储所有找到的内部链接
internal_links = []

# 遍历链接并点击
for link in links:
    # 使用JavaScript触发点击事件
    driver.execute_script("window.open(arguments[0]);", link.get_attribute("href"))

    # # 等待新窗口或标签页打开
    # time.sleep(5)

    # 切换到新窗口或标签页
    new_window_handles = [handle for handle in driver.window_handles if handle != main_window_handle]
    if len(new_window_handles) == 0:
        print("No new window opened.")
        continue

    driver.switch_to.window(new_window_handles[0])

    # 在新页面上找到所有特定的链接
    internal_page_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/jinrongshichangsi/147160/147289/147301/']")

    # 收集这些链接
    for internal_link in internal_page_links:
        internal_links.append(internal_link.get_attribute('href'))

    # 关闭当前窗口或标签页
    driver.close()

    # 切换回主窗口或标签页
    driver.switch_to.window(main_window_handle)

# 打印所有找到的内部链接
print("Found internal links:")
for internal_link in internal_links:
    print(internal_link)

# 关闭浏览器
driver.quit()
