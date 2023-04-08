extern crate reqwest;
extern crate scraper;
use scraper::{Html, Selector};
use std::fs::File;
use std::io::prelude::*;

fn main() {
    let url = "https://crypto.com/price";
    let response = reqwest::blocking::get(url).unwrap();
    let body = response.text().unwrap();
    let document = Html::parse_document(&body);

    let mut csv_data: Vec<Vec<String>> = Vec::new();

    let selector = Selector::parse(".chakra-text.css-13hqrwd").unwrap(); // price
    let mut prices: Vec<String> = Vec::new();
    for element in document.select(&selector) {
        prices.push(element.text().collect::<String>());
    }
    csv_data.push(prices);

    let selector2 = Selector::parse(".chakra-text.css-rkws3").unwrap(); // name
    let mut names: Vec<String> = Vec::new();
    for element in document.select(&selector2) {
        names.push(element.text().collect::<String>());
    }
    csv_data.push(names);

    let selector3 = Selector::parse(".chakra-text.css-yyku61").unwrap(); // 24H change
    let mut changes: Vec<String> = Vec::new();
    for element in document.select(&selector3) {
        changes.push(element.text().collect::<String>());
    }
    csv_data.push(changes);

    let selector4 = Selector::parse(".css-1nh9lk8").unwrap(); // 24H volume
    let mut volumes: Vec<String> = Vec::new();
    let mut counter = 0;
    for element in document.select(&selector4) {
        counter += 1;
        if counter % 2 == 1 {
            volumes.push(element.text().collect::<String>());
        }
    }
    csv_data.push(volumes);

    let selector5 = Selector::parse(".css-1nh9lk8").unwrap(); // market cap
    let mut caps: Vec<String> = Vec::new();
    let mut counter = 0;
    for element in document.select(&selector5) {
        counter += 1;
        if counter % 2 == 0 {
            caps.push(element.text().collect::<String>());
        }
    }
    csv_data.push(caps);

    // write to CSV file
    let mut file = File::create("crypto_data.csv").unwrap();
    for row in csv_data {
        let csv_row = row.join(",");
        file.write_all(csv_row.as_bytes()).unwrap();
        file.write_all("\n".as_bytes()).unwrap();
    }

    println!("Data written to crypto_data.csv");
}

