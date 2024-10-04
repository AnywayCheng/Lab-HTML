function toggleMenu() 
{
    var navbar = document.getElementById("navbar");
    navbar.classList.toggle("active");
}

function switchContent() 
{
    // 取得選單的值
    const selectedValue = document.getElementById("dropdown").value;
    
    // 隱藏所有區塊
    const blocks = document.getElementsByClassName("flexbox");
    for (let i = 0; i < blocks.length; i++) {
        blocks[i].style.display = "none";
    }
    
    // 顯示選中的區塊
    document.getElementById(selectedValue).style.display = "flex";
}
