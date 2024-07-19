import os
from PIL import Image

def resize_image(input_path, output_path, scale_factor, quality=85):
    """
    等比缩放图片

    :param input_path: 输入图片路径
    :param output_path: 输出图片路径
    :param scale_factor: 缩放比例
    """
    with Image.open(input_path) as img:
        # 获取原始尺寸
        width, height = img.size
        # 计算新尺寸
        new_width = int(width * scale_factor)
        new_height = int(height * scale_factor)
        # 重新调整图片尺寸
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)

        # 获取文件扩展名
        file_ext = os.path.splitext(output_path)[1].lower()

        # 保存图片到输出路径
        if file_ext in ['.jpg', '.jpeg']:
            resized_img.save(output_path, 'JPEG', quality=quality)
            print(f"width:{width} x height:{height},new_width:{new_width} x new_height:{new_height},quality:{quality}")
        else:
            resized_img.save(output_path)
            print(f"width:{width} x height:{height},new_width:{new_width} x new_height:{new_height}")

def batch_resize_images(input_dir, output_dir, scale_factor, quality=85):
    """
    批量等比缩放目录下的所有图片

    :param input_dir: 输入目录路径
    :param output_dir: 输出目录路径
    :param scale_factor: 缩放比例
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(('jpg', 'jpeg', 'png', 'bmp', 'gif')):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            resize_image(input_path, output_path, scale_factor, quality)
            print(f"Processed {filename}")

# 使用示例
input_directory = 'E:\\PaddleOcr_Images_Resize_I'
output_directory = 'E:\\PaddleOcr_Images_Resize_O'
scale_factor = 0.5  # 缩小为原来的50%
quality = 97  # JPEG保存质量

batch_resize_images(input_directory, output_directory, scale_factor, quality)