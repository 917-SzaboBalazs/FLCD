from symbolTable import SymbolTable

def test1():
    st = SymbolTable(10)
    st.insert("a", 10)
    st.insert("b", 5)

    assert(st.capacity() == 10)
    assert(st.size() == 2)
    assert(st.find("a") == 10)
    assert(st.find("b") == 5)
    assert(st.find("c") is None)

def test2():
    st = SymbolTable(20)
    st.insert("a", 10)
    st.insert("a", 12)

    assert(st.size() == 1)
    assert(st.find("a") == 12)

def test3():
    st = SymbolTable(10)
    st.insert("a", 10)
    st.insert("b", 15)
    st.remove("a")
    st.remove("c")

    assert(st.size() == 1)
    assert(st.find("a") is None)
    assert(st.find("b") == 15)
    assert(st.find("c") is None)

def test4():
    st = SymbolTable(10)
    st.insert("a", 10)
    st.insert("b", 15)
    st.remove("a")
    st.remove("c")
    st.insert("a", 20)

    assert(st.size() == 2)
    assert(st.find("a") == 20)
    assert(st.find("b") == 15)
    assert(st.find("c") is None)



test1()
test2()
test3()
test4()
