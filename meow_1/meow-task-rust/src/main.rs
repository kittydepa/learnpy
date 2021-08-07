// Crate UUID: https://docs.rs/uuid/0.8.2/uuid/



use uuid::Uuid;
fn main() -> Result<(), uuid::Error> {
    let my_uuid =
        Uuid::parse_str("936DA01F9ABD4d9d80C702AF85C822A8")?;
    println!("{}", my_uuid.to_urn());
    Ok(())
}
