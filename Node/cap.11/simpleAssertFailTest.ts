import { fail } from 'assert';

try {
    const value = 3;
    
    // Method fail is deprecated...
    fail(value, 4, 'Fails not equal', '==');
} catch (e) {
    console.log(e)
}
