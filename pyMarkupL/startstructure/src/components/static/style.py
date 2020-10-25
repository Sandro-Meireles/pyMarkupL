from pyMarkupL.core.elements import Element

class MyStyle(Element):

    def render(self, **kwargs):
        return """
<style>
    html, body {
        margin: 0px;
        padding: 0px;
        background-color: #c5d3f6;
    }
    .toolbar{
        box-shadow: 0px 1px 8px #0000003b;
        align-items: center;
        justify-content: center;
        display: flex;
        height: 8%;
        background-color: #6d7ae0;
        color: white;
    }
    .title {
        font-family: sans-serif;
        font-weight: bold;
        font-size: 30px;
    }

    .container{
        align-items: center;
        justify-content: center;
        display: flex;
        height: 92%;
        width: 100%;
    }

    .box{
        box-shadow: 4px 4px 6px #0000001a;
        background-color: white;
        height: 300px;
        width: 300px;
        margin: 5px;
        border-radius: 10px;
    }

    .box-title {
        border-radius: 10px 10px 0px 0px;
        background-color: #6d7ae0;
        height: 50px;
        display: flex;
        align-items: center;
        padding-left: 10px;
    }

    .box-title p {
        margin: 0px;
        color: white;
        font-family: sans-serif;
        letter-spacing: 1px;
    }

    .box-content {
        padding: 10px;
        text-align: start;
    }

    .box-content p{
        font-family: sans-serif;
        text-align: justify;
        color: #707070;
    }
</style>"""