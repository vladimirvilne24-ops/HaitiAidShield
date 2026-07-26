HaitiAidShield
Blockchain-Enabled Humanitarian Aid Governance Using Multi-Signature Smart Contracts and AI-Assisted Decision Support










HaitiAidShield Framework
                     HaitiAidShield

             Humanitarian Aid Request
                       │
                       ▼
                AI Sentry Analysis
                       │
                       ▼
        Trust Triangle Governance
      ┌────────┬──────────┬─────────┐
      │ Donor  │ Auditor  │ Local   │
      │        │          │ Trustee │
      └────────┴──────────┴─────────┘
                 │
          2 of 3 Approvals
                 │
                 ▼
       Solidity Smart Contract
                 │
                 ▼
      Polygon Amoy Blockchain
                 │
                 ▼
      Humanitarian Aid Recipient
Abstract

HaitiAidShield is an open-source blockchain governance framework designed to improve transparency, accountability, and auditability in humanitarian aid distribution. The project integrates Ethereum-compatible smart contracts, decentralized multi-signature governance, and AI-assisted decision support to reduce opportunities for corruption while preserving human oversight over financial decisions.

The prototype was developed as an independent cybersecurity and blockchain research project at Bridgewater State University and serves as the implementation accompanying the research paper submitted to the Silicon Valley Peace Conference.

Research Objectives
Develop a decentralized humanitarian aid governance framework.
Prevent unilateral fund disbursement.
Improve financial transparency.
Create immutable blockchain audit trails.
Demonstrate AI-assisted decision support.
Validate the framework through automated testing.
System Architecture
                 +---------------------+
                 | Aid Request         |
                 +----------+----------+
                            │
                            ▼
                 +---------------------+
                 | AI Sentry           |
                 | Risk Assessment     |
                 +----------+----------+
                            │
                            ▼
                 +---------------------+
                 | Trust Triangle      |
                 | 2-of-3 Governance   |
                 +----------+----------+
                            │
                            ▼
                 +---------------------+
                 | Smart Contract      |
                 +----------+----------+
                            │
                            ▼
                 +---------------------+
                 | Polygon Blockchain  |
                 +----------+----------+
                            │
                            ▼
                 +---------------------+
                 | Aid Recipient       |
                 +---------------------+
Project Components
HaitiAidShield
│
├── contracts/
│     HaitiAidShield.sol
│
├── scripts/
│     deploy.js
│
├── test/
│     HaitiAidShield.test.js
│
├── ai/
│     ai_sentry.py
│
├── ignition/
│
├── artifacts/
│
├── coverage/
│
├── hardhat.config.js
│
├── package.json
│
└── README.md
Governance Workflow
Aid Request

↓

Trustee Verification

↓

AI Risk Assessment

↓

Trustee Approval #1

↓

Trustee Approval #2

↓

Smart Contract Validation

↓

Fund Transfer

↓

Blockchain Event

↓

Immutable Audit Trail
AI Sentry Workflow
Aid Request

↓

Metadata Analysis

↓

GPS Validation

↓

Duplicate Detection

↓

Risk Calculation

↓

Risk Score

↓

Human Trustee Review
Smart Contract Functions
Function	Description
proposeAid()	Creates a humanitarian aid request
approveAid()	Records trustee approval
executeDisbursement()	Transfers approved funds
getContractBalance()	Returns contract balance
Security Features

✅ Multi-Signature Governance

✅ Immutable Blockchain Ledger

✅ Trustee Authorization

✅ Duplicate Approval Prevention

✅ Automated Fund Release

✅ AI-Assisted Risk Assessment

✅ Event Logging

✅ Transparent Audit Trail

Threat Model
Threat	Protection
Unauthorized access	Trustee authorization
Duplicate approvals	Smart contract validation
Insider fraud	Trust Triangle
Data tampering	Blockchain immutability
Unauthorized payments	Multi-signature approval
Suspicious requests	AI Sentry advisory analysis
Technology Stack
Technology	Purpose
Solidity 0.8.20	Smart contract development
Hardhat	Development and testing
Polygon Amoy	Blockchain deployment
Python	AI Sentry prototype
Web3.py	Blockchain interaction
GitHub	Open-source repository
Validation Results
Test	Status
Contract Deployment	✅ Passed
Trustee Initialization	✅ Passed
Aid Request Creation	✅ Passed
Unauthorized Trustee Rejected	✅ Passed
Duplicate Approval Prevention	✅ Passed
Multi-Signature Execution	✅ Passed
Contract Balance Verification	✅ Passed
Repository Statistics
Language: Solidity 0.8.20
Blockchain: Polygon Amoy Testnet
Testing Framework: Hardhat
Unit Tests: 7/7 Passed
Statement Coverage: 100%
Function Coverage: 100%
Line Coverage: 100%
Branch Coverage: 70.83%
Installation
git clone https://github.com/vladimirvilne24-ops/HaitiAidShield.git

cd HaitiAidShield

npm install
Compile
npx hardhat compile
Run Tests
npx hardhat test
Generate Coverage Report
npx hardhat coverage
Deploy to Polygon Amoy
npx hardhat run scripts/deploy.js --network amoy
Research Citation

If you use this repository in academic work, please cite:

Vilne, V. (2026). HaitiAidShield: Blockchain-Enabled Humanitarian Aid Governance Using Multi-Signature Smart Contracts and AI-Assisted Decision Support. Independent Research, Bridgewater State University. Submitted to the Silicon Valley Peace Conference.

Author

Vladimir Vilne

Independent Researcher
Department of Computer Science
Bridgewater State University

Research Interests:

Blockchain Security
Smart Contracts
Cybersecurity
Artificial Intelligence
Humanitarian Technology
Digital Governance
License

This project is released under the MIT License.
