# -*- coding:utf-8 -*-
# @Time   : 2023-08-30
# @Author : cniu6 (zerohh)
# @GitHub : https://github.com/cniu6/douyinpaging

from pynput import keyboard
import time

control = keyboard.Controller()


def on_press(key):
    # 按下按键时执行。
    # 通过属性判断按键类型。
    try:
        print('字母数字  {0} 按下'.format(
            key.char))
    except AttributeError:
        print('特殊的 {0} 按下'.format(
            key))
     


def on_release(key):
    # 松开按键时执行。
    print('{0} 释放'.format(
        key))

    

        # 如果监听是 page_up 就
    if key == keyboard.Key.page_up:
            time.sleep(0.5)
            control.press(keyboard.Key.up)
            time.sleep(0.01)
            control.release(keyboard.Key.up)
           

         # 如果监听是 page_down 就
    if key == keyboard.Key.page_down:
            time.sleep(0.5)
            control.press(keyboard.Key.down)
            time.sleep(0.01)
            control.release(keyboard.Key.down)
            


    # 如果监听是 "b" 就 在 0.2s内按下 alt+f3  快速关闭当前页面。  并且输出False退出程序。
    if key == keyboard.KeyCode.from_char('b') or key == keyboard.KeyCode.from_char('B'):
            control.press(keyboard.Key.alt_l)
            control.press(keyboard.KeyCode.from_vk(115))
            time.sleep(0.1)
            control.release(keyboard.Key.alt_l)
            control.release(keyboard.KeyCode.from_vk(115))
            # Stop listener 
            return False


    if key == keyboard.Key.esc:
        # Stop listener
        return False


print("=====================================")
print("翻页笔抖音 - 使用翻页笔 上下模拟键盘上下键 滑动 抖音短视频,快手,TIKTOK,SHOUTS,基本通用。")
print("by cniu6 (zerohh)       ")
print("")
print("仓库地址 https://github.com/cniu6/douyinpaging")
print("=====================================")
print("       ")
print("1. 使用翻页笔 上下模拟鼠标滚轮 滑动 抖音短视频。    ")
print("2. 翻页笔长按下键 <B>  快速关闭当前页面 并且 退出程序。   ")
print("3. 键盘版。 -- 点击延迟0.5s     ")
print("       ")
print("=====================================")
print("       ")
print("       ")

if __name__ == '__main__':
    # 监听keyboard
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

