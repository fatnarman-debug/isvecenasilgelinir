#!/bin/bash

# Function to fix a file at a specific depth
fix_file() {
    file=$1
    depth=$2
    
    if [ "$depth" -eq 1 ]; then
        # 1 level deep (e.g. hakkimizda/index.html)
        sed -i '' 's|href="assets/|href="../assets/|g' "$file"
        sed -i '' 's|src="assets/|src="../assets/|g' "$file"
        sed -i '' 's|href="index.html"|href="../"|g' "$file"
        sed -i '' 's|href="blog/index.html"|href="../blog/"|g' "$file"
        sed -i '' 's|href="hakkimizda.html"|href="../hakkimizda/"|g' "$file"
        sed -i '' 's|href="iletisim.html"|href="../iletisim/"|g' "$file"
        sed -i '' 's|href="hukuki-yardim.html"|href="../hukuki-yardim/"|g' "$file"
    elif [ "$depth" -eq 2 ]; then
        # 2 levels deep (e.g. blog/slug/index.html)
        sed -i '' 's|href="assets/|href="../../assets/|g' "$file"
        sed -i '' 's|src="assets/|src="../../assets/|g' "$file"
        sed -i '' 's|href="index.html"|href="../../"|g' "$file"
        sed -i '' 's|href="blog/index.html"|href="../"|g' "$file"
        sed -i '' 's|href="hakkimizda.html"|href="../../hakkimizda/"|g' "$file"
        sed -i '' 's|href="iletisim.html"|href="../../iletisim/"|g' "$file"
        sed -i '' 's|href="hukuki-yardim.html"|href="../../hukuki-yardim/"|g' "$file"
    fi
    
    # Global cleanup for any weird artifacts from previous failed attempts
    sed -i '' 's|blog/\.\./|../blog/|g' "$file"
    sed -i '' 's|\.\./\.\./\.\./\.\./|../../|g' "$file"
    sed -i '' 's|\.\./\.\./|../../|g' "$file" # Ensure no double replacements
    sed -i '' 's|index/|/|g' "$file"
    sed -i '' 's|\.html"|/"|g' "$file"
    sed -i '' 's|\.html#|/#|g' "$file"
    
    # Specific fix for blog index inside blog posts
    if [ "$depth" -eq 2 ]; then
        sed -i '' 's|href="\.\./"|href="../"|g' "$file"
    fi
}

# Fix root index.html separately
sed -i '' 's|hakkimizda\.html|hakkimizda/|g' index.html
sed -i '' 's|iletisim\.html|iletisim/|g' index.html
sed -i '' 's|hukuki-yardim\.html|hukuki-yardim/|g' index.html
sed -i '' 's|blog/index\.html|blog/|g' index.html
sed -i '' 's|index\.html|./|g' index.html

# Fix 1-level pages
for f in hakkimizda/index.html iletisim/index.html hukuki-yardim/index.html blog/index.html; do
    [ -f "$f" ] && fix_file "$f" 1
done

# Fix 2-level pages
for f in blog/*/index.html; do
    [ -f "$f" ] && fix_file "$f" 2
done
