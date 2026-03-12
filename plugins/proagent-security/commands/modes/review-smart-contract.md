# Review: Smart Contract Security

For Solidity smart contracts (reference: `agents/plugins/blockchain-web3/skills/solidity-security/SKILL.md`):

- Reentrancy vulnerabilities (external calls before state updates)
- Integer overflow/underflow without SafeMath or Solidity 0.8+ checks
- Access control issues (missing `onlyOwner`, unprotected `selfdestruct`)
- Unchecked return values from low-level calls
- Front-running vulnerabilities in DEX or auction contracts
- Gas griefing and denial of service vectors
