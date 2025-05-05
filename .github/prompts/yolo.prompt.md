# mode: 'ask'

# Expected output and any relevant constraints for this task.
# Always follow the syntax and guidelines mentioned below.





# 🇨🇭 SwissLang: A Zürich-Inspired Programming Language

SwissLang is a playful programming language inspired by the Zürich dialect of Swiss German. It combines local charm with unique syntax rules to create a distinctive developer experience. Below are the core language features, complete with explanations and examples.

---

## 🧠 Language Features & Examples

### 1. 🇨🇭 Swiss German Identifiers

Variable and function names should reflect the Zürich dialect to keep things authentically Swiss.

```plaintext
zämesetzig = 5 :TJ:

funktion rechneÖppis(wert) :TJ:
$
  gib zrugg wert + 1 :TJ:
$
```

---

### 2. 🧩 Custom Block Delimiters

Forget curly braces. In SwissLang, **`$`** is used to open and close code blocks.

```plaintext
IFFFFFFF zämesetzig > 4 :TJ:
$
  schriib("Zämesetzig is gross!") :TJ:
$
```

---

### 3. 🎯 Statement Ending

Every line in SwissLang must end with **`:TJ:`**, symbolizing Swiss precision and formality.

```plaintext
alter = 25 :TJ:
name = "Hans" :TJ:
```

---

### 4. 🔑 Custom Keywords

SwissLang replaces standard keywords with Swiss German-inspired alternatives.

#### Conditional Statements

- `IFFFFFFF` — replaces `if`
- `Elseeeeeee` — replaces `else`

```plaintext
IFFFFFFF alter < 18 :TJ:
$
  schriib("Du bisch nöd volljährig.") :TJ:
$
Elseeeeeee :TJ:
$
  schriib("Willkomme im Club!") :TJ:
$
```

#### Loop Statements (optional but expressive)

- `machewieder` — similar to `do...while`
- `fürjede` — similar to `for each`

```plaintext
machewieder :TJ:
$
  schriib("Noch einisch!") :TJ:
$

fürjede gericht in menu :TJ:
$
  schriib("I ha gärn " + gericht) :TJ:
$
```

---

## 🧪 Full Example Program

```plaintext
funktion begrüssig(name) :TJ:
$
  schriib("Hoi " + name + "! Wie gaht's?") :TJ:
$

zname = "Sandra" :TJ:
begrüssig(zname) :TJ:

alter = 17 :TJ:

IFFFFFFF alter < 18 :TJ:
$
  schriib("Sorry, nur für Erwachsene.") :TJ:
$
Elseeeeeee :TJ:
$
  schriib("Zäme zum Club!") :TJ:
$

menu = ["Rösti", "Fondue", "Schoggi"] :TJ:

fürjede gericht in menu :TJ:
$
  schriib("I ha gärn " + gericht) :TJ:
$
```

---

🎉 **SwissLang** brings fun, dialect, and discipline to your code. Ideal for lovers of Swiss German and creative coders alike.
