// Crate UUID: https://docs.rs/uuid/0.8.2/uuid/
// https://docs.diesel.rs/1.4.x/uuid/struct.Uuid.html
// https://docs.diesel.rs/1.4.x/uuid/struct.Uuid.html
// https://mozilla.github.io/mentat/apis/latest/rust/mentat/struct.Uuid.html



use uuid::Uuid;
fn main() -> Result<(), uuid::Error> {
    let my_uuid =
        Uuid::parse_str("936DA01F9ABD4d9d80C702AF85C822A8")?;
    println!("{}", my_uuid.to_urn());
    Ok(())
}
