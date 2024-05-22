document.addEventListener('DOMContentLoaded', function () {
    // element-one: Dupla kattintásra hozzáad egy "animation" class-t kattintáskor
    const elementOne = document.getElementById('element-one').addEventListener("dblclick" , function(){

        document.getElementById('element-one').classList.add("animation");
    })

    // element-two: Ha rámegy az egér, hozzáad egy box-shadow-t
    const elementTwo = document.getElementById('element-two').addEventListener("mousemove" , function(){
        document.getElementById('element-two').style.boxShadow = "0 5px  8px rgba(0,0,0,0.9)";
    })
    // element-three: Kattintásra eltűnik
    const elementThree = document.getElementById('element-three').addEventListener("click" , function(){
        document.getElementById('element-three').classList.add("hidden");
})
    // element-four: Kattintásra a háttere zöld lesz
    const elementFour = document.getElementById('element-four').addEventListener("click" , function(){
        document.getElementById('element-four').style.backgroundColor = "green";
})
    
})