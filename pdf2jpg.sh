# Set input and output paths
pdf_path="/config/Downloads/telegram-push-notifications/CIA_WorldFactBook-Political_world.pdf"
out_dir="/config/Downloads/telegram-push-notifications/maps"

# Create output directory if it doesn't exist
mkdir -p "$out_dir"

# Convert each page of PDF to PNG with 300 DPI
pdftoppm -png -r 300 "$pdf_path" "$out_dir/page"

# Rename the pages to page1.png, page2.png, etc.
page=1
for file in "$out_dir"/page*; do
    new_name="$out_dir/page$page.png"    
    mv "$file" "$new_name"
    let page=page+1
done
