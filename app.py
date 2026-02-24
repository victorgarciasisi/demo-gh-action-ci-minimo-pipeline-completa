from __future__ import annotations


def greet(name: str) -> str:
    clean_name = name.strip()
    if not clean_name:
        return "Hello!"
    return f"Hello, {clean_name}!"


def main() -> None:
    print(greet("DevSecOps"))


if __name__ == "__main__":
    main()
