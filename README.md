# aiogram_dialog da itemslar bilan tanishamiz
<hr>
<h3><a href="#installation">O'rnatish</a></h3>


<br id="installation">
    Ushbu branchda oddiy keyboard yozamiz va uni bosganda matn bilan javob beruvchi dastur yozamiz </br>
    Avvalo <b>MySG</b> nomli state hosil qilamiz. So'ng <b>Window</b> classi yordamida Inline tugmamizni hamda uning matnini <b>main_window</b> o'zgaruchisida saqlaymiz.</br>

    Const - Matn xabari yoziladi
    Button - tugma yoziladi,
    id - tugma bosilganda callback sifatida keluvchi id 
    state - state yoziladi
</p>



<code>Select</code> vidjetini Column ichida yoki Group ichida ham ishlatish mumkin
<code><pre>
Column(
    Select(
        # your code       
    )
)</pre>
</code>

> <code>Window</code> qismida esa, <code>getter=get_data</code> yoziladi va <code>Select</code> ham yoziladi.</br>

_Ba'zi bir o'zgaruvchilar:_
> - pos - elementlarning pozitsiyasini belgilaydi (1 dan boshlanadi)
> - data - <code>get_data</code> funksiyasidan qaytgan <code>dict</code> ni qaytaradi


