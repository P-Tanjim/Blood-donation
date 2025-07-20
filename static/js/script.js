const bar = document.getElementById('bar');
const close = document.getElementById('close');
const nav = document.getElementById('account-list');
const circles = document.querySelectorAll('.circle');
const status = document.querySelectorAll('.action')

if (bar){
    bar.addEventListener('click',() =>{
        nav.classList.add('active');
    })
}
if (close){
    close.addEventListener('click',() =>{
        nav.classList.remove('active');
    })
}

circles.forEach(circle => {
  const progress = circle.getAttribute('data-progress');
  circle.style.setProperty('--progress', progress);
});

status.forEach(actions => {
    const action = actions.getAttribute("data-progress"); // Corrected: actions instead of action
    let actionColor; // Declare a new variable to store the color

    if(action == "Approved"){
        actionColor = "green"; // Set the color to green if approved
    } else {
        actionColor = "red"; // Set the color to red if not approved
    }

    actions.style.setProperty('--color', actionColor); // Set the custom property
})
