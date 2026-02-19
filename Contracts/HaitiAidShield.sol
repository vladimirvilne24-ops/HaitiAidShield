// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/**
 * @title HaitiAidShield: Anti-Corruption Aid Distribution Framework
 * @author Vladimir Vilne
 * @notice This contract ensures that aid funds are only released when a consensus of trustees is reached.
 * @dev Implements a Multi-Signature and Immutable Event Logging system for transparency in high-risk zones.
 */
contract HaitiAidShield {
    
    // --- State Variables ---
    address[] public trustees; 
    uint public requiredSignatures;
    uint public totalAidDisbursed;
            
    struct AidRequest {
        string description;   
        uint amount;          
        address payable recipient; 
        uint approvalCount;
        bool executed;
        bool exists;
    }

    mapping(uint => AidRequest) public requests;
    mapping(uint => mapping(address => bool)) public isApproved; 
    uint public requestCount;

    // --- Events (The Immutable Audit Trail) ---
    event AidRequested(uint indexed requestId, string description, uint amount, address recipient);
    event AidApproved(uint indexed requestId, address indexed trustee);
    event AidDisbursed(uint indexed requestId, address recipient, uint amount);

    // --- Access Control ---
    modifier onlyTrustee() {
        bool authorized = false;
        for (uint i = 0; i < trustees.length; i++) {
            if (msg.sender == trustees[i]) {
                authorized = true;
                break;
            }
        }
        require(authorized, "Access Denied: Not a registered Trustee");
        _;
    }

    /**
     * @param _trustees The "Trust Triangle" (e.g., Donor, Auditor, Local Rep)
     * @param _required Minimum signatures needed (e.g., 2 of 3)
     */
    constructor(address[] memory _trustees, uint _required) {
        require(_trustees.length >= _required, "Signatures exceed trustee count");
        require(_required > 0, "At least one signature required");
        trustees = _trustees;
        requiredSignatures = _required;
    }

    receive() external payable {}

    /**
     * @notice Vladimir Vilne's Original Contribution: 
     * Proposes a transparent aid disbursement that requires multiple approvals.
     */
    function proposeAid(string memory _description, uint _amount, address payable _recipient) public onlyTrustee {
        requestCount++;
        AidRequest storage r = requests[requestCount];
        r.description = _description;
        r.amount = _amount;
        r.recipient = _recipient;
        r.executed = false;
        r.exists = true;

        emit AidRequested(requestCount, _description, _amount, _recipient);
    }

    function approveAid(uint _requestId) public onlyTrustee {
        require(requests[_requestId].exists, "Request does not exist");
        require(!requests[_requestId].executed, "Funds already disbursed");
        require(!isApproved[_requestId][msg.sender], "Trustee already approved this request");

        isApproved[_requestId][msg.sender] = true;
        requests[_requestId].approvalCount++;

        emit AidApproved(_requestId, msg.sender);

        if (requests[_requestId].approvalCount >= requiredSignatures) {
            executeDisbursement(_requestId);
        }
    }

    function executeDisbursement(uint _requestId) internal {
        AidRequest storage r = requests[_requestId];
        require(address(this).balance >= r.amount, "Insufficient contract balance");

        r.executed = true;
        totalAidDisbursed += r.amount;
        
        (bool success, ) = r.recipient.call{value: r.amount}("");
        require(success, "Transfer failed");

        emit AidDisbursed(_requestId, r.recipient, r.amount);
    }

    function getContractBalance() public view returns (uint) {
        return address(this).balance;
    }
}