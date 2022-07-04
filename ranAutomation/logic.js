function(e, t, r) {
    "use strict";
    r.d(t, "a", (function() {
        return o
    }
    ));
    var n = r(38);
    function o(e, t, r) {
        var o, i;
        if ("function" == typeof e.indexOf)
            switch (typeof t) {
            case "number":
                if (0 === t) {
                    for (o = 1 / t; r < e.length; ) {
                        if (0 === (i = e[r]) && 1 / i === o)
                            return r;
                        r += 1
                    }
                    return -1
                }
                if (t != t) {
                    for (; r < e.length; ) {
                        if ("number" == typeof (i = e[r]) && i != i)
                            return r;
                        r += 1
                    }
                    return -1
                }
                return e.indexOf(t, r);
            case "string":
            case "boolean":
            case "function":
            case "undefined":
                return e.indexOf(t, r);
            case "object":
                if (null === t)
                    return e.indexOf(t, r)
            }
        for (; r < e.length; ) {
            if (Object(n.a)(e[r], t))
                return r;
            r += 1
        }
        return -1
    }
}