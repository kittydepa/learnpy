// Will use package 'clap' instead: https://github.com/clap-rs/clap


// Below is an example from StackOverflow: https://stackoverflow.com/questions/26478558/working-with-uuid-in-rust
use uuid::Uuid; 


fn uuid_converter() {
    // if....then:
    //
}

fn device_id_converter() {
    // if... then:
    //
}

fn show_uuid(uuid: &Uuid) {
    //println!("bytes: {:?}", uuid.as_bytes());
    //println!("simple: {}", uuid.to_simple());
    println!("UUID: {}", uuid.to_hyphenated());
    //println!("urn: {}", uuid.to_urn());
}

fn main() {
    // // Generate a new UUID
    // let uuid = Uuid::new_v4();
    // show_uuid(&uuid); 

    // Parse an existing UUID
    let uuid = Uuid::parse_str("95022733-f013-301a-0ada-abc18f151006").unwrap();
    show_uuid(&uuid);
}


//  Take in command line input for the device ID/user ID, and it should be able to detect which one...
//      - if statements (if type == uuid.v4, if device ID is ___ characters long )
//      - using the UUID package for UUID data type, and clasp for command line/argparse
//  Write a function that converts UUID to Device ID, and vice versa