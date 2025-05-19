// Example: generate_insignia_metadata.js
// Run using: node generate_insignia_metadata.js

const fs = require('fs');
const path = require('path');

const insigniaDir = path.join(__dirname, 'metadata', 'insignia');
const description = "A Whisperseer Insignia. Identifies its bearer as an initiated Whisperseer Acolyte.";
const baseImageUrl = "https://raw.githubusercontent.com/TwilightLabsCrypto/WhisperseerAssets/refs/heads/main/images/";
const maxSupply = 100;

console.log(`Generating metadata files in ${insigniaDir}...`);

// Ensure directory exists
if (!fs.existsSync(insigniaDir)) {
    console.log(`Creating directory: ${insigniaDir}`);
    fs.mkdirSync(insigniaDir, { recursive: true });
}

for (let i = 1; i <= maxSupply; i++) {
    const metadata = {
        name: `Whisperseer Insignia #${i}`,
        description: description,
        image: `${baseImageUrl}insignia.png`
        // attributes: [] // Uncomment this line to include an empty attributes array initially
    };
    const filePath = path.join(insigniaDir, `${i}.json`);
    fs.writeFileSync(filePath, JSON.stringify(metadata, null, 2)); // Pretty print JSON
    // console.log(`Created/Updated ${filePath}`); // Uncomment for verbose logging
}

console.log(`Metadata generation complete for ${maxSupply} files.`); 