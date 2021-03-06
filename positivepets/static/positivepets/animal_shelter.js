/* client-side functions to populate html select elements for animal shelter page */

function loadMe(animal_array, breed_dict){

    var animalSelect = this.document.getElementById("animal_type");
    var breedSelect = this.document.getElementById("breed");

    var animal = localStorage.getItem("animalSelect")

    for (var i=0; i<animal_array.length; i++){
        var option = this.document.createElement("option");
        option.text = animal_array[i];
        animalSelect.add(option)
    }
    if (animal != null){
        animalSelect.value = animal;
    }
    fillBreeds(breed_dict);

    if (localStorage.getItem("breedSelect")){
        document.getElementById("breed").value = localStorage.getItem("breedSelect");
        document.getElementById("selected_breed").value = localStorage.getItem("breedSelect");
    }
    else{
        document.getElementById("breed").value =  breedSelect.value;
    }

    if (localStorage.getItem("animalSelect")){
        document.getElementById("animal_type").value = localStorage.getItem("animalSelect");
        document.getElementById("selected_animal").value = localStorage.getItem("animalSelect");
    }
    else{
        document.getElementById("selected_animal").value =  animalSelect.value;
    }
}

function fillBreedsJson(jsonObject){
    var breed_dict = JSON.parse(jsonObject)
    fillBreeds(breed_dict)
}

function fillBreeds(breed_dict){
    // get the selected animal
    var select_element = document.getElementById("animal_type");
    var animal;
    for (var i=0; i<select_element.length; i++){
        if (select_element.children[i].selected === true){
            animal = select_element.children[i].value;
            }
    }

    // get the list of pets  -- breed_dict is a dict of arrays; animal is the key
    var breed_array = breed_dict[animal]

    // populate the select element
    var breedSelect = document.getElementById("breed")
    breedSelect.innerHTML="";
    for (var i=0; i<breed_array.length; i++){
        var option = document.createElement("option");
        option.text = breed_array [i];
        breedSelect.add(option)
    }


    breed = localStorage.getItem("breedSelect")
    if (breed in breed_array){
        breedSelect.value = localStorage.getItem("breedSelect")
    }
    else{
        breedSelect.value = breed_array[0];
    }

    searchWords = localStorage.getItem("searchWordsSelect")
    var searchWordsSelect = document.getElementById("search_words")
    if (searchWords != null){
        searchWordsSelect.value = searchWords
    }
}

function makeBig(img_url, color){
    var elem = document.createElement("img");
    elem.setAttribute("src",img_url);
    var string1 = "<img src='";
    var string2 =  img_url
    var string3 = "' style='border-radius:5px; border: 5px solid "
    var string4 = color
    var string5 = " ; height:100%; width:100%; object-fit: cover;'>"
    fullstring = string1 + string2 + string3 + string4 + string5;

    document.getElementById("placehere").innerHTML = fullstring;
    document.getElementById("selected_image_url").value =  img_url;

}
function mouseOver(my_image){
    my_image.style.borderColor = "yellow";
}

function mouseOut(my_image, color){
    my_image.style.borderColor = color;
}

function saveState(){
    var animalSelect = document.getElementById("animal_type")
    localStorage.setItem("animalSelect",animalSelect.value)

    var breedSelect = document.getElementById("breed")
    localStorage.setItem("breedSelect",breedSelect.value)

    var searchWordsSelect = document.getElementById("search_words")
    localStorage.setItem("searchWordsSelect",searchWordsSelect.value)

    document.getElementById("selected_animal").value =  animalSelect.value;
    document.getElementById("selected_breed").value =  breedSelect.value;
    }