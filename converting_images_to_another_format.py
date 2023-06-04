from PIL import Image

# open initial image
initial_image_path_1 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_images\diagrama_don.png"
initial_image_path_2 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_images\diagrama_luh.png"
initial_image_path_3 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_images\don+luh.jpg"
initial_image_path_4 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_images\don_correlation.png"
initial_image_path_5 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_images\don_train_and_test_models.png"
initial_image_path_6 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_images\don_train_test.png"
initial_image_path_7 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_images\ires_don_2012_2018.jpg"
initial_image_path_8 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_images\ires_luh_2012_2018.jpg"
initial_image_path_9 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_images\luh_correlation.png"
initial_image_path_10 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_images\luh_train_and_test_models.png"
initial_image_path_11 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_images\luh_train_test.png"


image_1 = Image.open(initial_image_path_1)
image_2 = Image.open(initial_image_path_2)
image_3 = Image.open(initial_image_path_3)
image_4 = Image.open(initial_image_path_4)
image_5 = Image.open(initial_image_path_5)
image_6 = Image.open(initial_image_path_6)
image_7 = Image.open(initial_image_path_7)
image_8 = Image.open(initial_image_path_8)
image_9 = Image.open(initial_image_path_9)
image_10 = Image.open(initial_image_path_10)
image_11 = Image.open(initial_image_path_11)

# create new tiff  300 dpi
tiff_image_1 = image_1.copy()
tiff_image_2 = image_2.copy()
tiff_image_3 = image_3.copy()
tiff_image_4 = image_4.copy()
tiff_image_5 = image_5.copy()
tiff_image_6 = image_6.copy()
tiff_image_7 = image_7.copy()
tiff_image_8 = image_8.copy()
tiff_image_9 = image_9.copy()
tiff_image_10 = image_10.copy()
tiff_image_11 = image_11.copy()


save_tiff_path_1 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_to_tiff\diagrama_don.tiff"
save_tiff_path_2 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_to_tiff\diagrama_luh.tiff"
save_tiff_path_3 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_to_tiff\don+luh.tiff"
save_tiff_path_4 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_to_tiff\don_correlation.tiff"
save_tiff_path_5 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_to_tiff\don_train_and_test_models.tiff"
save_tiff_path_6 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_to_tiff\don_train_test.tiff"
save_tiff_path_7 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_to_tiff\ires_don_2012_2018.tiff"
save_tiff_path_8 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_to_tiff\ires_luh_2012_2018.tiff"
save_tiff_path_9 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_to_tiff\luh_correlation.tiff"
save_tiff_path_10 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_to_tiff\luh_train_and_test_models.tiff"
save_tiff_path_11 = "D:\disk_D\аспирантура\статья-про пожары\convert_images_from_png_to_tiff\converting\initial_to_tiff\luh_train_test.tiff"


tiff_image_1.save(save_tiff_path_1, dpi=(300, 300))
tiff_image_2.save(save_tiff_path_2, dpi=(300, 300))
tiff_image_3.save(save_tiff_path_3, dpi=(300, 300))
tiff_image_4.save(save_tiff_path_4, dpi=(300, 300))
tiff_image_5.save(save_tiff_path_5, dpi=(300, 300))
tiff_image_6.save(save_tiff_path_6, dpi=(300, 300))
tiff_image_7.save(save_tiff_path_7, dpi=(300, 300))
tiff_image_8.save(save_tiff_path_8, dpi=(300, 300))
tiff_image_9.save(save_tiff_path_9, dpi=(300, 300))
tiff_image_10.save(save_tiff_path_10, dpi=(300, 300))
tiff_image_11.save(save_tiff_path_11, dpi=(300, 300))


# close imagery
image_1.close()
image_2.close()
image_3.close()
image_4.close()
image_5.close()
image_6.close()
image_7.close()
image_8.close()
image_9.close()
image_10.close()
image_11.close()
tiff_image_1.close()
tiff_image_2.close()
tiff_image_3.close()
tiff_image_4.close()
tiff_image_5.close()
tiff_image_6.close()
tiff_image_7.close()
tiff_image_8.close()
tiff_image_9.close()
tiff_image_10.close()
tiff_image_11.close()