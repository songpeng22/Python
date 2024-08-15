from PIL import Image, ImageDraw, ImageFont
import cv2
import random
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import os
import string

# 生成一个前后五年内的随机日期
def generate_random_date():
    start_date = datetime.now() - timedelta(days=5*365)  # n年前
    end_date = datetime.now() + timedelta(days=3*365)    # n年后
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date #random_date.strftime('%Y/%m/%d')

# 随机一个字体文件，用于生成图片
def get_random_file_name(dir):
    #file_names = os.listdir(dir)
    file_names = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
    #print(file_names)
    random_file_name = random.choice(file_names)
    #print(f"random_font_file:{random_file_name}")
    return random_file_name

def get_fontsize_from_fontheight(font_path, target_height, text):
    # 初始字体大小
    fontsize = 10
    font = ImageFont.truetype(font_path, fontsize)
    
    # 创建临时图像以获取绘图对象
    temp_image = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(temp_image)

    while True:
        bbox = draw.textbbox((0, 0), text, font=font)
        height = bbox[3] - bbox[1]  # 计算高度
        if height > target_height:
            break
        fontsize += 1
        font = ImageFont.truetype(font_path, fontsize)

    return fontsize - 1

    
def get_choice():
    list = []
    list.append(0)
    list.append(1)
    list.append(2)
    list.append(3)

    #weights = [5,3,1,1]
    weights = [5,3,1,1]

    return random.choices(list,weights)[0]

def get_format(index):
    format_list_01 = []
    format_list_02 = []
    
    #
    format_list_01.append('%Y/%m/%d')
    format_list_01.append('%Y.%m.%d')
    format_list_01.append('%Y%m%d')
    format_list_01.append('%Y年%m月%d日')
    #
    format_list_02.append('%Y/%m/')
    format_list_02.append('%Y.%m.')
    format_list_02.append('%Y%m%d')
    format_list_02.append('%Y年%m月')

    #
    if index >= len(format_list_01):
        return ("","")

    return (format_list_01[index],format_list_02[index])
    
def generate_random_string():
    # 生成前四位大写字母
    letters = ''.join(random.choices(string.ascii_uppercase, k=3))
    # 生成后四位数字
    numbers = ''.join(random.choices(string.digits, k=4))
    # 拼接并返回最终字符串
    return letters + numbers

def generate_random_string(letter_probabilities):
    # 生成前四位大写字母
    letters = random.choices(
        population=list(letter_probabilities.keys()), 
        weights=list(letter_probabilities.values()), 
        k=0
    )
    
    # 生成后四位数字
    numbers = random.choices(string.digits, k=8)
    
    # 拼接结果
    return ''.join(letters) + ''.join(numbers)

# 定义每个大写字母的出现概率
probabilities = {
    'A': 8,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 12,
    'F': 2,
    'G': 2,
    'H': 6,
    'I': 0, # hard identify, not exist
    'J': 1,    
    'K': 1,
    'L': 4,
    'M': 2,
    'N': 6,
    'O': 0, # hard identify, not exist
    'P': 2,
    'Q': 1,
    'R': 5,
    'S': 6,
    'T': 9,
    'U': 3,
    'V': 1,
    'W': 2,
    'X': 1,
    'Y': 2,
    'Z': 1,           
}

# Load a TrueType or OpenType font file, and set the font size
font_name_Codystar_Regular = "Codystar-Regular-2.ttf"
font_root_path = "E:\\PaddleOCR_fonts\\"
font_Codystar_Light = font_root_path + "Codystar-Light-3.ttf"
font_Codystar_Regular = font_root_path + font_name_Codystar_Regular
font_Snapix = font_root_path + "snapix-1.ttf"
font_Ventouse = font_root_path + "Ventouse-1.ttf"
font_BPdotsLight = font_root_path + "BPdotsUnicase.otf"
font_BPdotsDiamondLight = font_root_path + "BPdotsUnicaseLight.otf"
font_Perfograma = font_root_path + "Perfograma.otf"
font_serif_dot_digital = font_root_path + "serif_dot_digital-7.ttf"
font_led_counter = font_root_path + "led_counter-7.ttf"

background_01 = "E:\\PaddleOCR_Images_Background\\Background_003.jpg"
background_02 = "E:\\PaddleOCR_Images_Background\\Background_007_sub01.jpg"
background_03 = "E:\\PaddleOCR_Images_Background\\Background_008_sub01.jpg"
background_04 = "E:\\PaddleOCR_Images_Background\\Background_012.jpg"
background_05 = "E:\\PaddleOCR_Images_Background\\Background_013.jpg"
background_06 = "E:\\PaddleOCR_Images_Background\\Background_015_sub01.jpg"
background_07 = "E:\\PaddleOCR_Images_Background\\Background_017.jpg"
background_08 = "E:\\PaddleOCR_Images_Background\\Background_018.jpg"
background_09 = "E:\\PaddleOCR_Images_Background\\Background_019.jpg"
background_10 = "E:\\PaddleOCR_Images_Background\\Background_031_sub012.png"
background_11 = "E:\\PaddleOCR_Images_Background\\Background_041_sub02.jpg"
# background with text
background_21 = "E:\\PaddleOCR_Images_Background\\Background_021_sub01.png"

offset = 65
position_x = 200
position_y = 10

BPdotsUnicase_x = 20
codestar_y = 60

font_size = 36
font_height = 24

column_01_x = 100
row_01_y = 60
column_02_x = 150
row_02_y = 120
column_03_x = 200
row_03_y = 180
column_04_x = 300
row_04_y = 240

position_01_x = column_02_x
position_01_y = codestar_y
position_02_x = 100
position_02_y = codestar_y
position_03_x = BPdotsUnicase_x
position_03_y = codestar_y
position_x = position_03_x
position_y = position_03_y

background_and_positions = [
    {
        "background": "E:\\PaddleOCR_Images_Background\\Background_003.jpg",
        "position": {"x": column_01_x, "y": row_01_y},
        "weight": 1
    },
    {
        "background": "E:\\PaddleOCR_Images_Background\\Background_004_sub01.jpg",
        "position": {"x": column_03_x, "y": row_03_y},
        "weight": 1
    },
    {
        "background": "E:\\PaddleOCR_Images_Background\\Background_007_sub01.jpg",
        "position": {"x": column_01_x, "y": row_01_y},
        "weight": 1
    },
    {
        "background": "E:\\PaddleOCR_Images_Background\\Background_008_sub01.jpg",
        "position": {"x": column_02_x, "y": row_02_y},
        "weight": 1
    },
    {
        "background": "E:\\PaddleOCR_Images_Background\\Background_012_sub01.jpg",
        "position": {"x": column_02_x, "y": row_02_y},
        "weight": 1
    },
    {
        "background": "E:\\PaddleOCR_Images_Background\\Background_013_sub01.jpg",
        "position": {"x": column_01_x, "y": row_01_y},
        "weight": 1
    },
    {
        "background": "E:\\PaddleOCR_Images_Background\\Background_015_sub01.jpg", #green background
        "position": {"x": column_01_x, "y": row_02_y},
        "weight": 0
    },
    {
        "background": "E:\\PaddleOCR_Images_Background\\Background_017.jpg",
        "position": {"x": column_02_x, "y": row_02_y},
        "weight": 1
    },
    {
        "background": "E:\\PaddleOCR_Images_Background\\Background_019_sub01.jpg", #green background
        "position": {"x": column_03_x, "y": row_03_y},
        "weight": 0
    },
    {
        "background": "E:\\PaddleOCR_Images_Background\\Background_031_sub012.png",
        "position": {"x": column_01_x, "y": row_01_y},
        "weight": 1
    },
    {
        "background": "E:\\PaddleOCR_Images_Background\\Background_041_sub02.jpg",
        "position": {"x": column_04_x, "y": row_03_y},
        "weight": 1
    },
    {
        "background": "E:\\PaddleOCR_Images_Background\\Background_051_sub01.jpg",
        "position": {"x": column_03_x, "y": row_03_y},
        "weight": 0
    },
    {
        "background": "E:\\PaddleOCR_Images_Background\\Background_021_sub01.png",
        "position": {"x": column_01_x, "y": row_01_y},
        "weight": 0
    }
]

def get_random_path_and_position(data):
    """
    根据权重随机取出一个路径和位置
    """
    weights = [item["weight"] for item in data]
    random_index = random.choices(range(len(data)), weights=weights, k=1)[0]
    return data[random_index]

# 生成字体文件
def generate_font_image(background,position_x,position_y,font_height,date,image_path,*font_paths):
    image = Image.open(background)
    draw = ImageDraw.Draw(image)
    
    # date text
    choice = get_choice()
    format_01,format02 = get_format(choice)
    date01 = date
    date02 = date + relativedelta(years=2)
    text_of_production_date = date01.strftime( format_01 )
    text_of_expiry_date = date02.strftime( format02 )
    # serial text
    serial_text = generate_random_string(probabilities) #generate_random_string()
    # specific text
    #serial_text = "20110832"
    #text_of_production_date = "2020/02/15"
    #text_of_expiry_date = "2023/01/"
    #print(f"serial_text:{serial_text}")
    # text list
    text_list = []
    text_list.append(serial_text)
    text_list.append(text_of_production_date)
    text_list.append(text_of_expiry_date)
    #for text in text_list:
    #    print(text)
    print(f"serial_text:{serial_text}")
    print(f"text_of_production_date:{text_of_production_date}")
    print(f"text_of_expiry_date:{text_of_expiry_date}")
    
    # font_path list length
    font_paths_len = len(font_paths)
    print(f"font_paths_len:{font_paths_len}")
    # font list
    font_list = []
    for font_path in font_paths:
        print(f"font_path:{font_path}")
        font_size = get_fontsize_from_fontheight(font_path,font_height,text_of_production_date)
        font = ImageFont.truetype(font_path, font_size)
        font_list.append(font)
        
    # font
    """
    font_path = font_paths[0]
    font_size = get_fontsize_from_fontheight(font_path,font_height,text_of_production_date)
    font_01 = ImageFont.truetype(font_path, font_size)
    print(f"font_path:{font_path}")

    font_path_ext_01 = font_paths[1]
    font_size_ext_01 = get_fontsize_from_fontheight(font_path_ext_01,font_height,text_of_production_date)
    font_ext_01 = ImageFont.truetype(font_path_ext_01, font_size_ext_01)
    print(f"font_path_font_path_ext_01ext:{font_path_ext_01}")
    
    font_path_ext_02 = font_paths[2]
    font_size_ext_02 = get_fontsize_from_fontheight(font_path_ext_02,font_height,text_of_production_date)
    font_ext_02 = ImageFont.truetype(font_path_ext_02, font_size_ext_02)
    print(f"font_path_ext_02:{font_path_ext_02}")
    """
    
    # position
    offset = 60
    position_01_x = position_x
    position_01_y = position_y
    position_01 = (position_01_x, position_01_y)
    position_02_x = position_x
    position_02_y = position_y + offset
    position_02 = (position_02_x, position_02_y)
    position_03_x = position_x
    position_03_y = position_y + offset*2
    position_03 = (position_03_x, position_03_y)
    # position list
    position_list = []
    position_list.append(position_01)
    position_list.append(position_02)
    position_list.append(position_03)

    # draw
    """
    """
    for (text,position) in zip(text_list,position_list):
        for char in text:
            if char in "":  # 特定数字
                font = font_list[1] if len(font_list) > 1 else font_list[0]
            elif char in "012358/":
                font = font_list[0] if len(font_list) > 1 else font_list[0]
            else:
                font = font_list[0]
            # 计算字符的边界框
            bbox = draw.textbbox(position, char, font=font)
            # 绘制字符
            draw.text(position, char, font=font, fill='black')
            # 更新 x 坐标
            position = (position[0] + bbox[2] - bbox[0],position[1])  # 使用边界框宽度更新位置
    
    #draw.text(position_01, serial_text, font=font_normal, fill="black")
    """
    font_01 = font_list[0]
    font_ext_01 = font_list[1]
    font_ext_02 = font_list[2]
    for char in serial_text:
        if char in "":  # 特定数字
            font = font_ext_01
        elif char in "012358/":
            font = font_ext_02
        else:
            font = font_01
        #draw.text((position_01_x,position_01_y), char, font=font, fill="black")
        # 计算字符的边界框
        bbox = draw.textbbox((position_01_x, position_01_y), char, font=font)
        # 绘制字符
        draw.text((position_01_x, position_01_y), char, font=font, fill='black')
        # 更新 x 坐标
        position_01_x += bbox[2] - bbox[0]  # 使用边界框宽度更新位置
    # text_of_production_date
    position_02_x = position_x
    position_02_y = position_y + offset
    position_02 = (position_02_x, position_02_y)
    #draw.text(position_02, text_of_production_date, font=font, fill="black")
    for char in text_of_production_date:
        if char in "":  # 特定数字
            font = font_ext_01
        elif char in "012358/":
            font = font_ext_02
        else:
            font = font_01
        #draw.text((position_02_x,position_02_y), char, font=font, fill="black")
        # 计算字符的边界框
        bbox = draw.textbbox((position_02_x, position_02_y), char, font=font)
        # 绘制字符
        draw.text((position_02_x, position_02_y), char, font=font, fill='black')
        # 更新 x 坐标
        position_02_x += bbox[2] - bbox[0]  # 使用边界框宽度更新位置
    # text_of_expiry_date
    position_03_x = position_x
    position_03_y = position_y + offset*2
    position_03 = (position_03_x, position_03_y)
    #draw.text(position_03, text_of_expiry_date, font=font_normal, fill="black")
    for char in text_of_expiry_date:
        if char in "2":  # 特定数字
            font = font_ext_01
        elif char in "012358/":
            font = font_ext_02
        else:
            font = font_01
        #draw.text((position_03_x,position_03_y), char, font=font, fill="black")
        # 计算字符的边界框
        bbox = draw.textbbox((position_03_x, position_03_y), char, font=font)
        # 绘制字符
        draw.text((position_03_x, position_03_y), char, font=font, fill='black')
        # 更新 x 坐标
        position_03_x += bbox[2] - bbox[0]  # 使用边界框宽度更新位置
    """
    # show image
    """
    
    import matplotlib.pyplot as plt
    plt.imshow(image)
    plt.show()
    cv2.waitKey(0)
    """
    basename = os.path.basename(font_path)
    date_text = date.strftime('%Y_%m_%d')
    image_name = basename + "_" + date_text + ".png"
    print(f"image_name:{image_name}")
    image_full_path = image_path +  image_name
    if not os.path.exists(image_full_path):
        image.save(image_full_path)
        print("图像:{image_full_path} 已保存")
    else:
        print(f"文件:{image_full_path} 已存在，跳过")

def generate_random_font_image(image_path,background,position_x,position_y):
    font_root_path = "E:\\PaddleOCR_fonts\\"
    font_ext_path = "E:\PaddleOCR_fonts\\font_ext\\"
    random_font_name = get_random_file_name(font_root_path)
    #ext_font_name = get_random_file_name(font_ext_path)
    ext_font_name_01 = "jd_lcd_rounded_FixB.ttf"
    ext_font_name_02 = "jd_lcd_rounded_FixC.ttf"
    print(f"random_font_name:{random_font_name}")
    #print(f"ext_font_name:{ext_font_name}")
    print(f"ext_font_name_01:{ext_font_name_01}")
    print(f"ext_font_name_02:{ext_font_name_02}")
    random_font_path = font_root_path + random_font_name #"snapix-1.ttf" #random_font_name
    #ext_font_path = font_ext_path + ext_font_name
    ext_font_path_01 = font_ext_path + ext_font_name_01
    ext_font_path_02 = font_ext_path + ext_font_name_02
    print(f"random_font_path:{random_font_path}")
    print(f"ext_font_path_01:{ext_font_path_01}")
    print(f"ext_font_path_02:{ext_font_path_02}")
    generate_font_image(background,position_x,position_y,font_height,generate_random_date(),image_path,*[random_font_path,ext_font_path_01,ext_font_path_02])
    #generate_font_image(background,position_x,position_y,font_height,generate_random_date(),image_path,*[random_font_path])

image_path_01 = "E:\\PaddleOCR_Data\\train_data_00_dot_font_test\\"
image_path_02 = "E:\\PaddleOCR_Data\\train_data_01_easy_test\\"
image_path_03 = "E:\\PaddleOCR_Data\\train_data_01_easy_test_03_BPdotsUnicase\\"
image_path_04 = "E:\\PaddleOCR_Data\\train_data_00_dot_font_test\\"
image_path_05 = "E:\\PaddleOCR_Data\\train_data_01_easy_test_04_SFTelegraphic\\"
image_path_06 = "E:\\PaddleOCR_Data\\train_data_01_easy_test_05_Collect_018\\"
image_path_07 = "E:\\PaddleOCR_Data\\train_data_01_code_insight\\"
image_path_08 = "E:\\PaddleOCR_Data\\train_data_01_line_close\\"

for i in range(4): #三种格式 200  #2024/05/01 120
    # 在这里执行你的代码
    random_path_and_position = get_random_path_and_position(background_and_positions)
    background = random_path_and_position["background"]
    position = random_path_and_position["position"]
    #generate_random_font_image(image_path_01,background_02,position_x,position_y)
    generate_random_font_image(image_path_08,background,position["x"],position["y"])
    pass
