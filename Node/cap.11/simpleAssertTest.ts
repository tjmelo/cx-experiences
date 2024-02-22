import { equal, ok } from 'assert';

const value = 3;

equal(true, value != 3, 'Test of value not equal');

// or
ok(value != 3, 'Test of value not equal');
