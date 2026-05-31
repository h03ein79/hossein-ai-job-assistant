function generate() {

    let text = document.getElementById("job").value;

    let words = text.match(/\b[A-Za-z]+\b/g);

    let filtered = words.filter(word =>
        word.length > 4
    );

    let counts = {};

    filtered.forEach(word => {

        word = word.toLowerCase();

        if (counts[word]) {
            counts[word]++;
        } else {
            counts[word] = 1;
        }

    });

    let sortedWords = Object.entries(counts)
        .sort((a, b) => b[1] - a[1]);

    let output = "<h2>Top ATS Keywords:</h2><ul>";

    sortedWords.forEach(item => {

        output += `<li>${item[0]} (${item[1]})</li>`;

    });

    output += "</ul>";

    document.getElementById("output").innerHTML = output;
}