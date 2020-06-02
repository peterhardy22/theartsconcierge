// SEARCH BAR VARIABLES
// creates variable for typing letters in the search bar on index.html
const searchInput = document.getElementById('search');
// MUSEUM/GALLERY VARIABLES
// grabs all of the museum/gallery names from index.html
const institutionNamesRaw = document.getElementsByClassName("institutionName");
// creates empty array for storing museum/gallery name strings
const institutionNames = []
// variable that stores museum/gallery name array length
const arrayLength = institutionNamesRaw.length;

// creates filter for search bar
searchInput.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase();
    for (let i = 0; i < arrayLength; i++) {
        if (institutionNames[i].includes(searchString) || searchString === undefined) {
            institutionNamesRaw[i].parentElement.style.display = 'block';
        } else {
            institutionNamesRaw[i].parentElement.style.display = 'none';
        }
    }
});

// loop to extract institution names
for (let i = 0; i < arrayLength; i++) {
    const institutions = institutionNamesRaw[i].textContent.toLowerCase();
    institutionNames.push(institutions);
}
