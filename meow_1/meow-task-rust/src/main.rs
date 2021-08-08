// Crate UUID: https://docs.rs/uuid/0.8.2/uuid/
// https://docs.diesel.rs/1.4.x/uuid/struct.Uuid.html
// https://docs.diesel.rs/1.4.x/uuid/struct.Uuid.html
// https://mozilla.github.io/mentat/apis/latest/rust/mentat/struct.Uuid.html

// About command line arguments in Rust, see ch. 12:
// https://doc.rust-lang.org/book/ch12-01-accepting-command-line-arguments.html

// Rust argparse package: https://github.com/tailhook/rust-argparse 


// ---------------------------------------------------------------------------------------------------------


// // Practice 1
// use uuid::Uuid;
// fn main() -> Result<(), uuid::Error> {
//     let my_uuid =
//         Uuid::parse_str("936DA01F9ABD4d9d80C702AF85C822A8")?;
//     println!("{}", my_uuid.to_urn());
//     Ok(())
// }

// // impl Uuid {
//     pub fn parse_str(input: &str) -> Result<Uuid, Error>
// }


// // Practice 2
// use std::env;

// fn main() {
//     let args: Vec<String> = env::args().collect();

//     let query = parse_config(&args); // Since the file name, which user does not need to write, takes up args[0]
//     //let filename = &args[2];

//     println!("Searching for {}", query);
//     //println!("In file {}", filename);
// }

// fn parse_config(args: &[String]) -> &str {
//     let query = &args[1];
//     query
// }


// // Practice 3 - Using argparse lib from u:tailhook on 
// extern crate argparse;

// use argparse::{ArgumentParser, StoreTrue, Store};

// fn main() {
//     let mut verbose = false;
//     let mut name = "World".to_string();
//    {
//        let mut ap = ArgumentParser::new();
//        ap.set_description("Greet someone.");
//        ap.refer(&mut verbose)
//            .add_option(&["-v", "--verbose"], StoreTrue,
//             "Be verbose");
//        ap.refer(&mut name)
//            .add_option(&["--name"], Store,
//         "Name for the greeting");
//        ap.parse_args_or_exit();
//    }

//    if verbose {
//        println!("name is {}", name);
//    }
//    println!("Hello {}!", name);
// }

// Practice 4
fn main() {
    
}