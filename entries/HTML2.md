# HTML

| File Suffix | Main Usage | Release | Current Version | Official Documentation |
| --- | --- | --- | --- | --- |
| .html | Creating Web Pages | 1992 | 5.2 | https://html.spec.whatwg.org/multipage/ |

# Basic Template

```html
<!DOCTYPE html>

<html lang="en">

    <head>
        <title>Title</title>
        <meta name="author" content="name">
        <meta name="description" content="Description of HTML document">
        <meta name="keywords" content="Keywords of HTML document">
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>

    <body>

        <header>
            Header part
        <header>

        <main>
            Main part
        <main>

        <footer>
            Footer part
        <footer>

    </body>

</html>

```

# Comments

| Symbols | Syntax | Description |
| --- | --- | --- |
| <!-- --> | <!-- comment --> | Declare block comment which will not be read as part of document |

# Layout Elements

| Tag | Syntax | Description | Parents |
| --- | --- | --- | --- |
| html | <html>document</html> | Mark entire HTML document | None |
| head | <head>meta_element</head> | Mark meta elements of HTML document | html |
| body | <body>visible_document</body> | Mark visible elements of HTML document | html |
| header | <header>header</header> | Mark header of HTML document | body |
| main | <main>main_part</main> | Mark main part of HTML document | body |
| footer | <footer>footer</footer> | Mark footer of HTML document | body |
| nav | <nav>navigation_bar</nav> | Mark navigation bar in HTML document | Inside body |
| div | <div>part</div> | Mark unspecified block element in HTML document | Inside body |
| span | <span>part</span> | Mark unspecified inline element in HTML document | Inside body |

# Meta Elements

| Tag | Syntax | Description | Parents |
| --- | --- | --- | --- |
| doctype | <!DOCTYPE html> | Declare document as HTML document at beginning of document | None |
| title | <title>document_title</title> | Declare title of HTML document | head |
| meta | <meta attributes> | Declare information about HTML document as attributes | head |
| link | <link href="source" rel="relationship"> | Insert content of external file to HTML via the attributes href and rel | head |
| style | <style>css_expressions</style> | Manipulate style of HTML document via CSS expressions | head |
| script | <script>javascript_expressions</script> | Manipulate behaviour of HTML document via JavaScript expressions | head |

# Order Elements

| Tag | Syntax | Description | Parents |
| --- | --- | --- | --- |
| h1 | <h1>heading</h1> | Mark heading of HTML document | Inside body |
| h2 | <h2>subheading</h2> | Mark subheading of HTML document | Inside h1 |
| h3 | <h3>subsubheading</h3> | Mark subsubheading of HTML document | Inside h2 |
| h4 | <h4>subsubsubheading</h4> | Mark subsubsubheading of HTML document | Inside h3 |
| h5 | <h5>subsubsubsubheading</h5> | Mark subsubsubsubheading of HTML document | Inside h4 |
| h6 | <h6>subsubsubsubsubheading</h6> | Mark subsubsubsubsubheading of HTML document | Inside h5 |
| p | <p>paragraph</p> | Mark paragraph of HTML document | Inside body |

# Style Elements

| Tag | Syntax | Description | Parents |
| --- | --- | --- | --- |
| br | <br> | Mark line break in HTML document | Inside body |
| b | <b>text</b> | Mark text as bold | Inside body |
| i | <i>text</i> | Mark text as italic | Inside body |
| u | <u>text</u> | Mark text as underlined | Inside body |

# Multimedia Elements

## Images

| Tag | Syntax | Description | Parents |
| --- | --- | --- | --- |
| img | <img src="image_source"> | Insert image in HTML document via the src attribute | Inside body |

## Audios

| Tag | Syntax | Description | Parents |
| --- | --- | --- | --- |
|  |  |  |  |

## Videos

| Tag | Syntax | Description | Parents |
| --- | --- | --- | --- |
| video | <video>video_element</video> | Insert video in HTML document | Inside body |
| source | <source src="video_source" type="video_format"> | Insert source of video from where to load via src attribute and specify video format via type attribute | video |

## Links

| Tag | Syntax | Description | Parents |
| --- | --- | --- | --- |
| a | <a href="source"> | Insert link in HTML document via src attribute | Inside body |

# Structured Elements

## Lists

| Tag | Syntax | Description | Parents |
| --- | --- | --- | --- |
| ul | <ul>unordered_list</ul> | Mark unordered list in HTML document | Inside body |
| ol | <ol>ordered_list</ol> | Mark ordered list in HTML document | Inside body |
| li | <li>list_item</li> | Mark item of list | ul, ol |

## Tables

| Tag | Syntax | Description | Parents |
| --- | --- | --- | --- |
| table | <table>table</table> | Mark table in HTML document | Inside body |
| thead | <thead>table_rows</thead> | Mark header rows of table in HTML document | table |
| tbody | <tbody>table_rows</tbody> | Mark main rows of table in HTML document | table |
| tfoot | <tfoot>table_rows</tfoot> | Mark footer rows of table in HTML document | table |
| tr | <tr>table_row</tr> | Mark row in table | Inside table |
| th | <th>table_header</th> | Mark header in table | tr |
| td | <td>table_cell</td> | Mark cell in table | tr |

## Forms

| Tag | Syntax | Description | Parents |
| --- | --- | --- | --- |
| form | <form action="link" method="method">form</form> | Mark form in HTML document according to the action and method attributes | Inside body |
| input | <input type="input_type"> | Insert box for inputting information in form according to the type attribute | form |
| textarea | <textarea>text</textarea> | Insert textbox for inputting large texts in form element | form |
| label | <label for="id">label</label> | Insert label for input element with same id in for attribute as in according id attribute of input element | form |
| button | <button type="button_type">button_name</button> | Insert button in form according to the type attribute | form |
| select | <select>menu</select> | Insert dropdown menu in form | form |
| datalist | <datalist>menu</datalist> | Display pre-defined options as autocomplete feature in form | form |
| option | <option value="item">item</option> | Insert item to dropdown menu according to the value attribute | select, datalist |

# Attributes

## General Attributes

| Attribute | Syntax | Values | Description | Tags |
| --- | --- | --- | --- | --- |
| name | name="name" | - | Declare intern name of element. Inside an input tag, name will be a parameter as part of a GET-request for the action attribute of the form tag (if the input element has an input field, the input will be the value of the parameter). | Every tag |
| lang | lang="value" | "en" (language is english)
"de" (language is german) | Declare language of element | Every tag |
| id | id="id_name" | - | Declare unique id of element | Every tag |
| class | class="class_name" | - | Declare class of element | Every tag |
| property | property="information" | - | Insert information about tag for script | Every tag |
| type | type="value" | "video/format” (type is video in format for video tag)

"text" (type is textbox for input tag)
"number" (type is number selector for input tag)
"search" (type is search bar for input tag)
"password" (type is search bar for input tag)
"button" (type is a clickable button for input tag)
"radio" (type is a radio button for input tags with same name)
"checkbox" (type is a checkbox button for input tag)
"hidden" (input for user is hidden and not interactable for input tag)

"submit" (type is submit button for button tag) | Declare format of block | video, input, button |
| href | href="source" | - | Declare adresse of link to lead to | a, link |
| src | src="source" | - | Declare source of element from where to load | img, script |

## Meta Attributes

| Attribute | Syntax | Values | Description | Tags |
| --- | --- | --- | --- | --- |
| content | content="information" | - | Insert information about HTML document via meta tag | meta |
| rel | rel="value" | "stylesheet" (file is stylesheet of document) | Declare relationship of external file to HTML document via link | meta |
| charset | charset="value" | "UTF-8" (Characters are in UTF-8 decoded) | Declare decoding of characters in HTML document via meta tag | meta |

## Style Attributes

| Attribute | Syntax | Values | Description | Tags |
| --- | --- | --- | --- | --- |
| style | style="css_expression" | - | Manipulate design of tag via CSS expressions | Every tag |
| width | width="value" | "numberpx" (width as pixels of screen)
"device-width" (width is width of device) | Command elements width | Inside body |
| height | height="value" | "numberpx" (height as pixels of screen) | Command elements height | Inside body |

## Multimedia Attributes

| Attribute | Syntax | Values | Description | Tags |
| --- | --- | --- | --- | --- |
| alt | alt="description" | - | Declare alternative description if media could not load | img |
| autoplay | autoplay | - | Command media to play automatically | video |
| loop | loop | - | Command media to play repeatedly | video |
| muted | muted | - | Command media to mute audio | video |

## Structured Elements Attributes

| Attribute | Syntax | Values | Description | Tags |
| --- | --- | --- | --- | --- |
| colspan | colspan="number" | - | Cell of table spans about number of columns | th, td |
| rowspan | rowspan="number" | - | Cell of table spans about number of rows | th, td |
| action | action="link" | - | Command form to execute link by submitting form | form |
| method | method="value" | "get" (GET-method for link to follow)
"post" (POST-method for link to follow) | Method of accompanying action attribute | form |
| onsubmit | onsubmit="javascript_command" | - | Command form to execute JavaScript command when submitted | form |
| placeholder | placeholder="text" | - | Insert placeholder text inside input box | input |
| autocomplete | autocomplete="value" | "off" (turn history of typed characters of) | Handle additional functions of input box | input |
| autofocus | autofocus | - | Place cursor automatically inside input box | input |
| required | required | - | Input must be filled to submit form | input |
| list | list=”list_id” |  | Link input element to datalist element with list id as id | input |
| value | value="value" | - | Specifies internal value of an element.
For input elements with type button, reset and submit it sets the displayed text.
For input elements with type text, password and hidden it defines the initial value of the unput field.
For input elements with type checkbox, radio and image it defines the value of the unput and gets send on submit. | input, option |
| selected | selected | - | Select option automatically inside of dropdown menu | option |
| disabled | disabled | - | Make option unusable inside of dropdown menu | option |
| min | min="number" | - | Set minimal value for input element of type number | input |
| max | max="number" | - | Set maximal value for input element of type number | input |
| rows | rows="number" | - | Set number of rows for textarea element | textarea |
| cols | cols="number" | - | Set number of columns for textarea element | textarea |

## Event Attributes

| Attribute | Syntax | Values | Description | Tags |
| --- | --- | --- | --- | --- |
| onclick | onclick="js_function" | - | Executing JavaScript function by clicking | Inside body |
| onsubmit | onsubmit="js_function" | - | Executing JavaScript function by submitting | Inside body |
| onchange | onchange="js_function" | - | Executing JavaScript function if value of element element is changed | Inside body |