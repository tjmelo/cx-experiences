module.exports = {
    'Test 1': ({expect, equal, notEqual, done}) => {
        expect(4);
        equal(true, Array.isArray([]));
        equal(true, Array.isArray([1,2,3]));
        equal(true, Array.isArray(new Array(3)));
        notEqual(true, 1 > 2);
        done();
    },
    'Test 2': ({expect, deepEqual, ok, done}) => {
        expect(2);
        deepEqual([1,2,3], [1,2,3]);
        ok('str' === 'str', 'equal');
        done();
    }
}
