/*==================================================
      PHISHGUARD AI
      Developer : Pravin Chavda
===================================================*/

console.clear();

console.log("%c🛡 PHISHGUARD AI",
"color:cyan;font-size:28px;font-weight:bold;");

console.log("%cCyber Security Project",
"color:#00ff99;font-size:16px;");

console.log("%cDeveloper : PRAVIN CHAVDA",
"color:yellow;font-size:15px;");

console.log("-------------------------------------");


// =====================================
// Page Loaded
// =====================================

document.addEventListener("DOMContentLoaded",function(){

    console.log("Website Loaded Successfully");

    welcomeMessage();

    typingEffect();

    inputAnimation();

    buttonAnimation();

    updateClock();

    randomTip();

    setInterval(updateClock,1000);

});


// =====================================
// Welcome Message
// =====================================

function welcomeMessage(){

    setTimeout(function(){

        showNotification(
            "🛡 Welcome to PhishGuard AI"
        );

    },500);

}



// =====================================
// Notification
// =====================================

function showNotification(message){

    let note=document.createElement("div");

    note.className="notification";

    note.innerHTML=message;

    document.body.appendChild(note);

    setTimeout(function(){

        note.classList.add("show");

    },100);

    setTimeout(function(){

        note.classList.remove("show");

        setTimeout(function(){

            note.remove();

        },500);

    },3500);

}



// =====================================
// Typing Effect
// =====================================

function typingEffect(){

    let title=document.querySelector(".title");

    if(!title) return;

    let text=title.innerText;

    title.innerHTML="";

    let i=0;

    function type(){

        if(i<text.length){

            title.innerHTML+=text.charAt(i);

            i++;

            setTimeout(type,50);

        }

    }

    type();

}



// =====================================
// Input Animation
// =====================================

function inputAnimation(){

    let input=document.querySelector("input");

    if(!input) return;

    input.addEventListener("focus",function(){

        input.style.boxShadow="0 0 20px cyan";

    });

    input.addEventListener("blur",function(){

        input.style.boxShadow="";

    });

}



// =====================================
// Button Animation
// =====================================

function buttonAnimation(){

    let buttons=document.querySelectorAll("button");

    buttons.forEach(btn=>{

        btn.addEventListener("click",function(){

            btn.innerHTML="Scanning...";

            btn.disabled=true;

            setTimeout(function(){

                btn.disabled=false;

                btn.innerHTML="🔍 Scan Website";

            },2000);

        });

    });

}



// =====================================
// History Toggle
// =====================================

function toggleHistory(){

    let history=document.getElementById("historyBox");

    if(!history) return;

    if(history.style.display==="block"){

        history.style.display="none";

    }

    else{

        history.style.display="block";

    }

}



// =====================================
// Digital Clock
// =====================================

function updateClock(){

    let clock=document.getElementById("clock");

    if(!clock) return;

    let now=new Date();

    clock.innerHTML=now.toLocaleTimeString();

}



// =====================================
// Random Cyber Tips
// =====================================

let tips=[

"✔ Never click unknown email links.",

"✔ Always verify HTTPS.",

"✔ Enable Two Factor Authentication.",

"✔ Don't share OTP.",

"✔ Keep Browser Updated.",

"✔ Use Strong Passwords.",

"✔ Avoid Public WiFi for Banking.",

"✔ Scan suspicious URLs before opening."

];

function randomTip(){

    let tip=document.getElementById("tip");

    if(!tip) return;

    let i=0;

    tip.innerHTML=tips[i];

    setInterval(function(){

        i++;

        if(i>=tips.length){

            i=0;

        }

        tip.innerHTML=tips[i];

    },5000);

}



// =====================================
// Result Glow
// =====================================

function resultGlow(result){

    let box=document.getElementById("resultBox");

    if(!box) return;

    if(result==="safe"){

        box.style.boxShadow="0 0 25px lime";

    }

    else if(result==="warning"){

        box.style.boxShadow="0 0 25px orange";

    }

    else{

        box.style.boxShadow="0 0 25px red";

    }

}



// =====================================
// Progress Animation
// =====================================

function animateProgress(id,value){

    let bar=document.getElementById(id);

    if(!bar) return;

    let width=0;

    let timer=setInterval(function(){

        if(width>=value){

            clearInterval(timer);

        }

        else{

            width++;

            bar.style.width=width+"%";

            bar.innerHTML=width+"%";

        }

    },15);

}



// =====================================
// Password Strength
// =====================================

function passwordStrength(score){

    if(score>=80){

        return "Strong";

    }

    else if(score>=50){

        return "Medium";

    }

    else{

        return "Weak";

    }

}



// =====================================
// URL Validation
// =====================================

function validateURL(url){

    let pattern=/^(https?:\/\/)/;

    return pattern.test(url);

}



// =====================================
// Fake Loading Effect
// =====================================

function loading(){

    let loader=document.getElementById("loader");

    if(!loader) return;

    loader.style.display="block";

    setTimeout(function(){

        loader.style.display="none";

    },1800);

}



// =====================================
// Footer Year
// =====================================

let year=document.getElementById("year");

if(year){

    year.innerHTML=new Date().getFullYear();

}



// =====================================
// Cyber Quote
// =====================================

const quotes=[

"Security is everyone's responsibility.",

"Think Before You Click.",

"Stay Alert Stay Secure.",

"Protect Your Digital Identity.",

"Cyber Awareness Starts With You."

];

console.log(
quotes[Math.floor(Math.random()*quotes.length)]
);



// =====================================
// End
// =====================================

console.log("Script Loaded Successfully.");