import medical_data_visualizer

# Load dan preprocess data
df = medical_data_visualizer.load_data()
df = medical_data_visualizer.preprocess_data(df)

# Buat dan tampilkan grafik kategori
fig_cat = medical_data_visualizer.draw_cat_plot(df)
fig_cat.show()

# Buat dan tampilkan heatmap
fig_heat = medical_data_visualizer.draw_heat_map(df)
fig_heat.show()
