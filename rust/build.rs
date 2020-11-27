extern crate gcc;

fn main () {
    println!("cargo:rustc-flags=-L ./lib");
}