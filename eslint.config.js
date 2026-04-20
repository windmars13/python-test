// eslint.config.js
import js from '@eslint/js';
import prettier from 'eslint-config-prettier';

export default [
  js.configs.recommended,
  prettier,
  {
    // ✅ 加這段：宣告執行環境的全域變數
    languageOptions: {
      globals: {
        // Browser 全域
        window: 'readonly',
        document: 'readonly',
        console: 'readonly',
        navigator: 'readonly',
        alert: 'readonly',
        fetch: 'readonly',
        // Node.js 全域
        process: 'readonly',
        require: 'readonly',
        module: 'readonly',
        __dirname: 'readonly',
      },
      ecmaVersion: 'latest',
      sourceType: 'module',
    },
    rules: {
      'no-var': 'error',
      'prefer-const': 'error',
      'no-unused-vars': ['warn', { argsIgnorePattern: '^_' }],
      eqeqeq: ['error', 'always'],
      'no-console': 'warn', // warn 不是 error，不會擋 commit
      'no-debugger': 'error',
      'prefer-template': 'error',
      'object-shorthand': 'error',
    },
    ignores: ['node_modules/', 'dist/', 'build/', '*.min.js'],
  },
];
