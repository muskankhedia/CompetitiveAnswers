func {
    int t = 0;
    List<Integer> l1 = new ArrayList<Integer>(); 
    for (int i = 0; i < indexArray.size(); i++) {
        t = t*  indexArray.get(i)
    }

    for (int i = 0; i < indexArray.size(); i++) {

        if (indexArray.get(i) != 0) {
            x = t /  indexArray.get(i)
        } else {
            x = 1;
            for (int j = 0; j < indexArray.size(); j++) {
                x = x *  indexArray.get(j)
            }
        }
        l1.add(x)
    }

    return l1;

}